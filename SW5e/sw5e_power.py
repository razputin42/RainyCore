from ..listable_element import BaseListableEntry
from ..base_entry_types import BasePower


class PowerSW5e(BaseListableEntry, BasePower):
    def get_casting_time(self):
        return self.get("castingPeriodText", "N/A")

    def get_range(self):
        return self.get("range", "N/A")

    def get_duration(self):
        return self.get("duration", "N/A")

    def get_classes(self):
        return self.get("classes", "")

    def get_level(self):
        return self.get("level", "0")


