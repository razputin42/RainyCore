from ..listable_element import BaseListableEntry


class ItemSW5e(BaseListableEntry):
    def value_conversion(self, value):
        return float(value)

    def get_type(self):
        return self.get_attributes()["type"]

    def get_rarity(self):
        return self.get_attributes()["searchableRarity"]

    def get_description(self):
        return self.get_attributes()["text"]

    def matches(self, **attribute_requirements):
        for key, value in attribute_requirements.items():
            if key == "rarity" and value != self.get_rarity():
                return False
            elif key == "type" and value != self.get_type():
                return False
        return True