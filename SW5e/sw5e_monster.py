from ..listable_element import BaseListableEntry
from ..base_entry_types import BaseMonster


class MonsterSW5e(BaseListableEntry, BaseMonster):
    class Behavior(BaseMonster.Behavior):
        def get_text(self):
            return self.get("text", "N/A")

    def get_size(self):
        return self.get("size", "N/A")

    def get_type(self):
        return self.get("types", ["N/A"])

    def get_alignment(self):
        return self.get("alignment", "N/A")

    def get_armor_class(self):
        return self.get("armorClass", "N/A")

    def get_hit_points(self):
        return self.get("hitPoints", "N/A")

    def get_speed(self):
        return self.get("speeds", "N/A")

    def get_strength(self):
        return self.get("strength", "N/A")

    def get_strength_modifier(self):
        return self.get("strengthModifier", "N/A")

    def get_dexterity(self):
        return self.get("dexterity", "N/A")

    def get_dexterity_modifier(self):
        return self.get("dexterityModifier", "N/A")

    def get_constitution(self):
        return self.get("constitution", "N/A")

    def get_constitution_modifier(self):
        return self.get("constitutionModifier", "N/A")

    def get_intelligence(self):
        return self.get("intelligence", "N/A")

    def get_intelligence_modifier(self):
        return self.get("intelligenceModifier", "N/A")

    def get_wisdom(self):
        return self.get("wisdom", "N/A")

    def get_wisdom_modifier(self):
        return self.get("wisdomModifier", "N/A")

    def get_charisma(self):
        return self.get("charisma", "N/A")

    def get_charisma_modifier(self):
        return self.get("charismaModifier", "N/A")

    def get_saving_throws(self):
        return self.get("savingThrows", "N/A")

    def get_resistances(self):
        return self.get("damageResistances", "N/A")

    def get_immunities(self):
        return self.get("damageImmunities", "N/A")

    def get_condition_immunities(self):
        return self.get("conditionImmunities", "N/A")

    def get_skills(self):
        return self.get("skills", "N/A")

    def get_senses(self):
        return self.get("senses", "N/A")

    def get_languages(self):
        return self.get("languages", "N/A")

    def get_experience(self):
        return self.get("experiencePoints", "N/A")

    def get_challenge_rating(self):
        return self.get("challengeRating", "-1")

    def is_srd_valid(self):
        return True

    def get_behaviors(self):
        for behavior in self.get("behaviors", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_actions(self):
        for behavior in self.get("behavior", []):
            yield MonsterSW5e.Behavior(**behavior)

    def get_legendary_actions(self):
        for behavior in self.get("legendaryBehavior", []):
            yield MonsterSW5e.Behavior(**behavior)
