from ..listable_element import BaseListableEntry
from ..base_entry_types import BaseMonster


class MonsterSW5e(BaseListableEntry, BaseMonster):
    def get_challenge_rating(self):
        return self.get("challengeRating", "-1")

    def is_srd_valid(self):
        return True
