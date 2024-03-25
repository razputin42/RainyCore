import logging
import re
from string import Template

from ..base_entry_types import BaseMonster, MonsterHTMLFormatDict
from ..dice import dice
from ..listable_element import BaseListableEntry
from ..signals import sNexus


class MonsterSW5e(BaseListableEntry, BaseMonster):
    class Behavior(BaseMonster.Behavior):
        @property
        def attack_bonus(self):
            return self.get("attackBonus", None)

        @property
        def damage_dice(self):
            return self.get("damageRoll", None)

        @property
        def description(self):
            return self.get("description", None)

        def roll(self):
            to_hit = None
            if self.attack_bonus is not None:
                to_hit, _ = dice("d20")
                to_hit += self.attack_bonus
            logging.debug(f"Rolled {to_hit} to hit")
            damage_dice = self.damage_dice.strip().lower()
            damage = 0
            for damage_die in damage_dice.split("+"):
                rolled, _ = dice(damage_die)
                damage += rolled
            logging.debug(f"Rolled {damage} damage")
            return to_hit, damage

        @property
        def type(self):
            return self.get("monsterBehaviorType", None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        updated_types = []
        for type in self.get_type():
            updated_types.append(type.capitalize())
        self._attributes["types"] = updated_types

        if self.get_challenge_rating() == "CR":  # broken entry
            self._attributes["challengeRating"] = "-1"


    def get_size(self):
        return self.get("size", None)

    def get_type(self):
        return self.get("types", None)

    def get_alignment(self):
        return self.get("alignment", None)

    def get_armor_class(self):
        return self.get("armorClass", None)

    def get_hit_points(self):
        return self.get("hitPoints", None)

    def get_speed(self):
        return self.get("speeds", None)

    def get_strength(self):
        return self.get("strength", None)

    def get_strength_modifier(self):
        return self.get("strengthModifier", None)

    def get_dexterity(self):
        return self.get("dexterity", None)

    def get_dexterity_modifier(self):
        return self.get("dexterityModifier", None)

    def get_constitution(self):
        return self.get("constitution", None)

    def get_constitution_modifier(self):
        return self.get("constitutionModifier", None)

    def get_intelligence(self):
        return self.get("intelligence", None)

    def get_intelligence_modifier(self):
        return self.get("intelligenceModifier", None)

    def get_wisdom(self):
        return self.get("wisdom", None)

    def get_wisdom_modifier(self):
        return self.get("wisdomModifier", None)

    def get_charisma(self):
        return self.get("charisma", None)

    def get_charisma_modifier(self):
        return self.get("charismaModifier", None)

    def get_saving_throws(self):
        return self.get("savingThrows", None)

    def get_resistances(self):
        return self.get("damageResistances", None)

    def get_immunities(self):
        return self.get("damageImmunities", None)

    def get_condition_immunities(self):
        return self.get("conditionImmunities", None)

    def get_skills(self):
        return self.get("skills", None)

    def get_senses(self):
        value = self.get("senses", None)
        if value == ["-"]:
            return None
        return value

    def get_languages(self):
        value = self.get("languages", None)
        if value == ["-"]:
            return None
        return value

    def get_experience(self):
        return self.get("experiencePoints", None)

    def get_challenge_rating(self):
        return self.get("challengeRating")

    def get_behaviors(self):
        for behavior in self.get("behaviors", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_actions(self):
        for behavior in self.get("behavior", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_legendary_actions(self):
        behaviors = self.get_behaviors()
        return [behavior for behavior in behaviors if behavior.type == "Legendary"]

    def get_traits(self):
        behaviors = self.get_behaviors()
        return [behavior for behavior in behaviors if behavior.type == "Trait"]

    def get_actions(self):
        behaviors = self.get_behaviors()
        return [behavior for behavior in behaviors if behavior.type == "Action"]

    def perform_attack(self, attack):
        logging.debug(f"Performing attack {attack.get_name()}, {attack.get_description()}")
        sNexus.attackSignal.emit(self, attack)

    def to_html(self):
        if not self.is_srd_valid():
            # What to display if entry is not SRD valid
            template = Template(MonsterHTMLFormatDict["not_srd"])
            return template.safe_substitute(
                name=self.get_name()
            )

        # this is going to get confusing fast... This is everything before saving throws
        template = Template(MonsterHTMLFormatDict['first'])
        html = template.safe_substitute(
            name=self.get_name(),
            size=self.get_size(),
            type=", ".join(self.get_type()),
            alignment=self.get_alignment(),
            armor_class=self.get_armor_class(),
            hit_points=self.get_hit_points(),
            speed=self.get_speed(),
            str=self.get_strength(),
            str_mod=self.get_strength_modifier(),
            dex=self.get_dexterity(),
            dex_mod=self.get_dexterity_modifier(),
            con=self.get_constitution(),
            con_mod=self.get_constitution_modifier(),
            int=self.get_intelligence(),
            int_mod=self.get_intelligence_modifier(),
            wis=self.get_wisdom(),
            wis_mod=self.get_wisdom_modifier(),
            cha=self.get_charisma(),
            cha_mod=self.get_charisma_modifier()
        )
        descriptive_list = [
            ("Saving Throws", self.get_saving_throws()),
            ("Damage Resistance", self.get_resistances()),
            ("Damage Immunities", self.get_immunities()),
            ("Condition Immunities", self.get_condition_immunities()),
            ("Skills", self.get_skills()),
            ("Senses", self.get_senses()),
            ("Languages", self.get_languages()),
        ]
        for name, value in descriptive_list:
            if value is None:
                continue
            if isinstance(value, list):
                value = ", ".join(value)
            template = Template(MonsterHTMLFormatDict['desc'])
            html = html + template.safe_substitute(
                name=name,
                desc=value
            )

        template = Template(MonsterHTMLFormatDict['cr'])
        html = html + template.safe_substitute(
            cr=self.get_challenge_rating(),
            xp=self.get_experience()
        )
        html = html + MonsterHTMLFormatDict['gradient']

        # Add traits behaviors
        for trait in self.get_traits():
            template = Template(MonsterHTMLFormatDict['action_even'])
            html = html + template.safe_substitute(
                name=trait.get_name(),
                text=trait.get_description().replace("\n", "<br/>")
            )

        # second part of the self
        template = Template(MonsterHTMLFormatDict['second'])
        html = html + template.safe_substitute()

        # add attack behaviors action
        for itt, action in enumerate(self.get_actions()):
            if itt % 2 == 0:  # even
                template = Template(MonsterHTMLFormatDict['action_even'])
            else:
                template = Template(MonsterHTMLFormatDict['action_odd'])
            html = html + template.safe_substitute(
                name=action.get_name(),
                text=action.get_description()
            )

        # add each legendary action
        legendary_actions = list(self.get_legendary_actions())
        if len(legendary_actions) != 0:
            html = html + MonsterHTMLFormatDict['legendary_header']
        for itt, action in enumerate(legendary_actions):
            if itt % 2 == 0:  # even
                template = Template(MonsterHTMLFormatDict['action_even'])
            else:
                template = Template(MonsterHTMLFormatDict['action_odd'])
            html = html + template.safe_substitute(
                name=action.get_name(),
                text=action.get_description()
            )
        template = Template(MonsterHTMLFormatDict['rest'])
        html = html + template.safe_substitute()
        return html
