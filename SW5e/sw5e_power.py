from ..listable_element import BaseListableEntry
from ..base_entry_types import BasePower


class PowerSW5e(BaseListableEntry, BasePower):
    def get_level(self):
        return self.get("level", "0")
