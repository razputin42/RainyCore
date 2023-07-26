import re
import copy
from PyQt5.QtCore import pyqtSignal, QObject
from .signals import sNexus
import math

xp_dict = {
    "00": 0,
    "0": 10,
    "1/8": 25,
    "1/4": 50,
    "1/2": 100,
    "1": 200,
    "2": 450,
    "3": 700,
    "4": 1100,
    "5": 1800,
    "6": 2300,
    "7": 2900,
    "8": 3900,
    "9": 5500,
    "10": 5900,
    "11": 7200,
    "12": 8400,
    "13": 10000,
    "14": 11500,
    "15": 13000,
    "16": 15000,
    "17": 18000,
    "18": 20000,
    "19": 22000,
    "20": 25000,
    "21": 33000,
    "22": 41000,
    "23": 50000,
    "24": 62000,
    "25": 75000,
    "26": 90000,
    "27": 105000,
    "28": 120000,
    "29": 135000,
    "30": 155000
}

size_dict = dict(
    T="Tiny",
    S="Small",
    M="Medium",
    L="Large",
    H="Huge",
    G="Gargantuan",
    A="Medium"
)


class BaseAction:
    def __init__(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_text(self):
        raise NotImplementedError

    def is_attack(self):
        raise NotImplementedError


class Monster:
    def __init__(self):
        raise NotImplementedError

    def addSpells(self):
        sNexus.addSpellsSignal.emit(self.extract_spellbook())

    def add_to_encounter(self, n=1):
        sNexus.addMonstersToEncounter.emit(self, n)

    def copy(self):
        return copy.deepcopy(self)

    def perform_attack(self, attack):
        sNexus.attackSignal.emit(self.name, attack.attack)

    def append_source(self, source):
        self.source.append(source)

    def __str__(self):
        return self.name

    def get_actions(self):
        raise NotImplementedError

    def get_traits(self):
        raise NotImplementedError

    def get_legendaries(self):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError

    def get_alignment(self):
        raise NotImplementedError

    def get_ac(self):
        raise NotImplementedError

    def get_hp(self):
        raise NotImplementedError

    def get_speed(self):
        raise NotImplementedError

    def get_str(self):
        raise NotImplementedError

    def get_str_modifier(self):
        raise NotImplementedError

    def get_dex(self):
        raise NotImplementedError

    def dex_modifier(self):
        raise NotImplementedError

    def get_con(self):
        raise NotImplementedError

    def get_con_modifier(self):
        raise NotImplementedError

    def get_int(self):
        raise NotImplementedError

    def get_int_modifier(self):
        raise NotImplementedError

    def get_wis(self):
        raise NotImplementedError

    def get_wis_modifier(self):
        raise NotImplementedError

    def get_cha(self):
        raise NotImplementedError

    def get_challenge_rating(self):
        raise NotImplementedError

    def get_experience(self):
        raise NotImplementedError

    def get_saves(self):
        raise NotImplementedError

    def get_resistances(self):
        raise NotImplementedError

    def get_immunities(self):
        raise NotImplementedError

    def get_condition_immunities(self):
        raise NotImplementedError

    def get_skills(self):
        raise NotImplementedError

    def get_senses(self):
        raise NotImplementedError

    def get_languages(self):
        raise NotImplementedError

    def handle_duplicate(self, existing_entry, resource):
        existing_entry.append_source(resource)


class Monster35(Monster):
    def __init__(self, entry, idx):
        self.entry = entry
        self.index = idx
        for attr in entry:
            if attr.tag == "hit_dice":
                HD, hp_no_dice = self.extract_hp(attr.text)
                hp_no_dice = hp_no_dice.replace(' hp', '')
                self.HD = HD
                self.hp_no_dice = hp_no_dice
            elif attr.tag == "challenge_rating":
                self.cr = re.sub("[^,;0-9/]+", "", attr.text)
            elif attr.tag == "initiative":
                self.initiative = int(attr.text.split(" ")[0])
            else:
                setattr(self, attr.tag, attr.text)


class Monster5e(Monster):
    database_fields = [
        'name', 'size', 'type', 'alignment', 'ac', 'hp', 'speed',
        ['str', 'dex', 'con', 'int', 'wis', 'cha'],
        'save', 'resist', 'immune', 'conditionImmune', 'skill', 'senses', 'languages', 'passive', 'cr', 'spells'
    ]
    required_database_fields = ['name', 'str', 'dex', 'con', 'int', 'wis', 'cha']

    class Action(BaseAction):
        database_fields = ['name', 'text', 'attack']

        def __init__(self, attr):
            s = ""
            for itt, _attr in enumerate(attr):
                if _attr.tag == "text":
                    if _attr.text is None:
                        s = s + "<br>"
                    else:
                        s = s + _attr.text
                        if itt != 0 and itt != len(attr) - 1:
                            s = s + "<br>"
                else:
                    setattr(self, _attr.tag, _attr.text)
            self.text = s

            if not hasattr(self, "attack"):
                if hasattr(self, "name"):
                    print(f"- {self.name}")
                bonus_to_hit_raw = re.findall("[+-]?\d to hit", self.text)
                damage_raw = re.findall("Hit:? \d* \(\d*d\d*[+-]?\d*\)", self.text)
                if bonus_to_hit_raw:
                    bonus_to_hit_raw = bonus_to_hit_raw[0]
                    bonus_to_hit = bonus_to_hit_raw[:bonus_to_hit_raw.find(" ")]
                if damage_raw:
                    damage_raw = damage_raw[0]
                    damage = damage_raw[damage_raw.find("(") + 1:damage_raw.find(")")]

                if not bonus_to_hit_raw and not damage_raw:
                    pass
                elif not bonus_to_hit_raw:  # area of attack
                    self.attack = f"{damage_raw}"
                else:
                    self.attack = f"{bonus_to_hit},{damage}"

        def __str__(self):
            if self.name is None:
                return self.text
            else:
                return self.name + ": " + self.text

    class Trait(Action):
        pass

    def __init__(self, entry, idx, srd_list=None):
        super().__init__()
        self.source = []
        self.entry = entry
        self.index = idx
        self.action_list = []
        self.trait_list = []
        self.legendary_list = []
        if entry is not None:
            for attr in entry:
                if attr.text is None:
                    setattr(self, attr.tag, attr.text)
                elif attr.tag == "trait":
                    self._add_trait(attr)
                elif attr.tag == "action":
                    self._add_action(attr)
                elif attr.tag == "legendary":
                    self._add_legendary(attr)
                elif attr.tag == "size":
                    size = attr.text.upper()
                    if size in size_dict.keys():
                        self.size = size_dict[size]
                    else:
                        self.size = attr.text
                elif attr.tag == "type" and attr.text is not None and ',' in attr.text:
                    temp_list = attr.text.split(",")
                    self.type = ",".join(temp_list[:-1]).strip().lower()
                    if 'swarm' in self.type.lower():
                        self.type = 'Swarm'
                    self.source = [temp_list[-1]]
                    if "(" in self.type:
                        subtype_raw = self.type[self.type.find("(") + 1:self.type.find(")")]
                        subtype_list = subtype_raw.split(", ")
                        self.subtype = []
                        for subtype in subtype_list:
                            self.subtype.append(subtype.strip())
                elif attr.tag == "source":
                    self.source = [attr.text]
                else:
                    setattr(self, attr.tag, attr.text)
            if hasattr(self, 'cr') and self.cr is not None:
                self.xp = xp_dict[self.cr]
            else:
                self.xp = 0
            if hasattr(self, 'dex') and self.dex is not None:
                self.initiative = self.calculate_modifier(self.dex)
            if hasattr(self, 'hp') and self.hp is not None:
                self.hp_no_dice, self.HD = self.extract_hp(self.hp)

            self.__srd_valid = srd_list is None or self.name in srd_list
        else:
            self.name = ""
            self.size = ""
            self.type = ""
            self.alignment = ""
            self.ac = ""
            self.hp = ""
            self.speed = ""
            self.str = 0
            self.dex = 0
            self.con = 0
            self.wis = 0
            self.int = 0
            self.cha = 0
            self.cr = ""
            self.xp = 0
            self.__srd_valid = True

    @staticmethod
    def extract_hp(hp):
        if hp is None:
            return "", ""
        i = hp.find("(")
        if i != -1:
            j = hp.find(")")
            hp_no_dice = hp[0:i]
            HD = hp[i + 1:j]
        else:
            hp_no_dice = ""
            HD = ""
        return hp_no_dice, HD

    @staticmethod
    def calculate_modifier(score, sign=False):
        if score is None:
            return 0
        score = int(score)
        mod = math.floor((score - 10) / 2)
        if sign:
            if mod > 0:
                return "+" + str(mod)
        return mod

    def _add_action(self, attr):
        print(self.name)
        action = self.Action(attr)
        self.action_list.append(action)

    def _add_trait(self, attr):
        trait = self.Trait(attr)
        self.trait_list.append(trait)

    def _add_legendary(self, attr):
        legendary = self.Action(attr)
        self.legendary_list.append(legendary)

    def is_srd_valid(self):
        return self.__srd_valid

    def extract_spellbook(self):
        return_list = []
        if hasattr(self, "spells") and self.spells is not None:
            for s in self.spells.split(","):
                return_list.append(s.strip().replace('*', ''))
            return return_list
        else:
            return None


# class MonsterSW5e(Monster):
#     required_database_fields = [
#         'name', 'size', 'types', 'alignment', 'armorClass', 'hitPoints', 'speed', 'strength', 'strengthModifier',
#         'dexterity', 'dexterityModifier', 'constitution', 'constitutionModifier', 'intelligence',
#         'intelligenceModifier', 'wisdom', 'wisdomModifier', 'charisma', 'charismaModifier'
#     ]
#
#     class Behavior(BaseAction):
#         def __init__(self, **kwargs):
#             for key, value in kwargs.items():
#                 setattr(self, key, value)
#
#         def get_name(self):
#             return self.name
#
#         def get_text(self):
#             return self.description
#
#         def is_attack(self):
#             return self.attackType == "MeleeWeapon"
#
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             if key == "behaviors":
#                 self.behaviors = [MonsterSW5e.Behavior(**behavior) for behavior in value]
#             else:
#                 setattr(self, key, value)
#
#     def is_srd_valid(self):
#         return True
#
#     def get_actions(self):
#         return self.behaviors
#
#     def get_traits(self):
#         return []
#
#     def get_legendaries(self):
#         return []
#
#     def get_name(self):
#         return self.name
#
#     def get_size(self):
#         return self.size
#
#     def get_type(self):
#         return ", ".join(self.types)
#
#     def get_alignment(self):
#         return self.alignment
#
#     def get_ac(self):
#         return self.armorClass
#
#     def get_hp(self):
#         return self.hitPoints
#
#     def get_speed(self):
#         return self.speed
#
#     def get_str(self):
#         return self.strength
#
#     def get_str_modifier(self):
#         return self.strengthModifier
#
#     def get_dex(self):
#         return self.dexterity
#
#     def dex_modifier(self):
#         return self.dexterityModifier
#
#     def get_con(self):
#         return self.constitution
#
#     def get_con_modifier(self):
#         return self.constitutionModifier
#
#     def get_int(self):
#         return self.intelligence
#
#     def get_int_modifier(self):
#         return self.intelligenceModifier
#
#     def get_wis(self):
#         return self.wisdom
#
#     def get_wis_modifier(self):
#         return self.wisdomModifier
#
#     def get_cha(self):
#         return self.charisma
#
#     def get_cha_modifier(self):
#         return self.charismaModifier
#
#     def get_challenge_rating(self):
#         return self.challengeRating
#
#     def get_experience(self):
#         return self.experiencePoints
#
#     def get_saves(self):
#         if self._is_empty("savingThrows"):
#             return None
#         return ", ".join(self.savingThrows)
#
#     def get_resistances(self):
#         if self._is_empty("damageResistances"):
#             return None
#         return ", ".join(self.damageResistances)
#
#     def get_immunities(self):
#         if self._is_empty("damageImmunities"):
#             return None
#         return ", ".join(self.damageImmunities)
#
#     def get_condition_immunities(self):
#         if self._is_empty("conditionImmunities"):
#             return None
#         return ", ".join(self.conditionImmunities)
#
#     def get_skills(self):
#         if self._is_empty("skills"):
#             return None
#         return ", ".join(self.skills)
#
#     def get_senses(self):
#         if self._is_empty("senses"):
#             return None
#         return ", ".join(self.senses)
#
#     def get_languages(self):
#         if self._is_empty("languages"):
#             return None
#         return ", ".join(self.languages)
#
#     def _is_empty(self, key):
#         if not hasattr(self, key):
#             return None
#         value = getattr(self, key)
#         return value == ["-"] or value == [] or value is None
