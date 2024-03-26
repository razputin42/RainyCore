import copy
import re


class Item:
    required_database_fields = ['name', 'rarity']
    database_fields = ['name', 'type', 'magic', 'value', 'weight', 'ac', 'strength', 'stealth', 'text']
    damage_type_dict = dict(
        P="Piercing",
        S="Slashing",
        B="Bludgeoning"
    )

    type_dict = {
        "A": "Ammunition",
        "G": "General",
        "HA": "Heavy Armor",
        "LA": "Light Armor",
        "M": "Melee",
        "MA": "Medium Armor",
        "P": "Potion",
        "R": "Ranged",
        "RD": "Rod",
        "RG": "Ring",
        "S": "Shield",
        "SC": "Scroll",
        "ST": "Staff",
        "W": "Wondrous",
        "WD": "Wand",
        "$": "Valuables"
    }

    magic_dict = {
        "0": "No",
        "1": "Yes"
    }

    def __init__(self, entry, idx, srd_list):
        self.entry = entry
        self.index = idx
        self.rarity = "N/A"
        s = ""
        for attr in entry:
            if attr.tag == "magic":
                if attr.text is not None and attr.text in self.magic_dict.keys():
                    self.magic = self.magic_dict[attr.text]
                else:
                    self.magic = "No"
            elif attr.tag == "text":
                if attr.text is None:
                    s = s + "<br>"
                else:
                    s = s + attr.text.replace("\n", "<br>")
            elif attr.tag == "type" and attr.text in self.type_dict.keys():
                self.type = self.type_dict[attr.text]
            elif attr.tag == "name" and " GP - " in attr.text:
                self.name = attr.text.split(" GP - ")[1]
            elif attr.tag == "value":
                if attr.text is None:
                    self.value = None
                    continue
                self.value = self.value_conversion(attr.text)
            elif attr.tag == "source":
                self.source = [attr.text]
            elif attr.tag == "detail":  # new database has rarirty listed as detail, for some unknown reason
                self.rarity = re.sub("(, cursed)? \(.*\)$", "", attr.text.capitalize())
            else:
                setattr(self, attr.tag, attr.text)
        self.text = s
        self.__srd_valid = srd_list is None or self.name in srd_list

    def __str__(self):
        return self.name

    def value_conversion(self, value):
        conversion = [("cp", 0.01), ("sp", 0.1), ("gp", 1), ("pp", 10), ("ep", 100)]
        for denoter, factor in conversion:
            if denoter in value:
                self.value = float(value.strip(denoter)) * factor
                break

    def is_srd_valid(self):
        return self.__srd_valid

    def copy(self):
        return copy.deepcopy(self)

    def append_source(self, source):
        self.source.append(source)

    def handle_duplicate(self, existing_entry, resource):
        existing_entry.append_source(resource)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


class Item35(Item):
    of_list = ['Scroll', 'Wand']

    def __init__(self, entry, idx):
        self.entry = entry
        self.index = idx
        for attr in entry:
            if attr.tag == 'category' and attr.text in self.of_list:
                self.name = attr.text + ' of ' + self.name
            else:
                setattr(self, attr.tag, attr.text)
