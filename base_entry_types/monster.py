class BaseMonster:
    def get_challenge_rating(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError

    def get_alignment(self):
        raise NotImplementedError

    def get_armor_class(self):
        raise NotImplementedError

    def get_hit_points(self):
        raise NotImplementedError

    def get_speed(self):
        raise NotImplementedError

    def get_strength(self):
        raise NotImplementedError

    def get_strength_modifier(self):
        raise NotImplementedError

    def get_dexterity(self):
        raise NotImplementedError

    def get_dexterity_modifier(self):
        raise NotImplementedError

    def get_constitution(self):
        raise NotImplementedError

    def get_constitution_modifier(self):
        raise NotImplementedError

    def get_intelligence(self):
        raise NotImplementedError

    def get_intelligence_modifier(self):
        raise NotImplementedError

    def get_wisdom(self):
        raise NotImplementedError

    def get_wisdom_modifier(self):
        raise NotImplementedError

    def get_charisma(self):
        raise NotImplementedError

    def get_charisma_modifier(self):
        raise NotImplementedError

    def get_saving_throws(self):
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

    def get_experience(self):
        raise NotImplementedError
