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
                    s = s + attr.text + "<br>"
            elif attr.tag == "type" and attr.text in self.type_dict.keys():
                self.type = self.type_dict[attr.text]
            elif attr.tag == "name" and " GP - " in attr.text:
                self.name = attr.text.split(" GP - ")[1]
            elif attr.tag == "value":
                if attr.text is None:
                    self.value = None
                    continue
                conversion = [("cp", 0.01), ("sp", 0.1), ("gp", 1), ("pp", 10), ("ep", 100)]
                for denoter, factor in conversion:
                    if denoter in attr.text:
                        self.value = float(attr.text.strip(denoter)) * factor
                        break
            elif attr.tag == "source":
                self.source = [attr.text]
            elif attr.tag == "detail":  # new database has rarirty listed as detail, for some unknown reason
                self.rarity = re.sub("(, cursed)? \(.*\)$", "", attr.text.capitalize())
            else:
                setattr(self, attr.tag, attr.text)
        self.text = s
        if srd_list is None or self.name in srd_list:
            self.srd = "yes"
        else:
            self.srd = "no"
        self.srd_bool = self.srd == "yes"

    def __str__(self):
        return self.name

    def copy(self):
        return copy.deepcopy(self)

    def append_source(self, source):
        self.source.append(source)

    def __str__(self):
        return "Item"


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
