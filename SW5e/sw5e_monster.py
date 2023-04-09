from ..listable_element import BaseListableEntry
from ..base_entry_types import BaseMonster


class MonsterSW5e(BaseListableEntry, BaseMonster):
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
        return self.get("challengeRating", "-1")

    def get_behaviors(self):
        for behavior in self.get("behaviors", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_actions(self):
        for behavior in self.get("behavior", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_legendary_actions(self):
        for behavior in self.get("legendaryBehavior", []):
            yield MonsterSW5e.Behavior(**behavior)
