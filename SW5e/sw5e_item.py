from ..listable_element import BaseListableEntry


class ItemSW5e(BaseListableEntry):
    def value_conversion(self, value):
        return float(value)
