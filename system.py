from .monster import MonsterSW5e, Monster
from .item import ItemSW5e, Item
from .spell import PowerSW5e, Spell
from enum import Enum

SW5e_plaintext = "SW5e"
DnD5e_plaintext = "DnD5e"


class System(Enum):
    DnD5e = 0
    SW5e = 1

    def __eq__(self, other):
        return self.name == other.name

    def is_DnD5e(self):
        return self == System.DnD5e

    def is_SW5e(self):
        return self == System.SW5e

    def get_system_classes(self):
        if self == System.SW5e:
            return MonsterSW5e, ItemSW5e, PowerSW5e
        elif self == System.DnD5e:
            return Monster, Item, Spell

    @staticmethod
    def to_plaintext(system):
        if system == System.SW5e:
            return SW5e_plaintext
        elif system == System.DnD5e:
            return DnD5e_plaintext
        raise IOError

    @staticmethod
    def from_plaintext(s):
        if s == SW5e_plaintext:
            return System.SW5e
        elif s == DnD5e_plaintext:
            return System.DnD5e
        raise IOError

    def system_flags(self):
        flags = dict(
            loot_widget=True
        )
        if self.is_SW5e():
            flags["loot_widget"] = False
        return flags




