import copy


school_dict = dict(
    A="Abjuration",
    C="Conjuration",
    N="Necromancy",
    EV="Evocation",
    T="Transmutation",
    D="Divinition",
    I="Illusion",
    EN="Enchantment"
)

class Spell:
    required_database_fields = ["name"]
    database_fields = [
        'name', 'level', 'school', 'time', 'range', 'components', 'duration', 'text'
    ]

    def __init__(self, entry, idx, srd_list):
        self.entry = entry
        self.index = idx
        s = ""
        for attr in entry:
            if attr.tag == "text":
                if attr.text is None:
                    s = s + "<br>"
                else:
                    s = s + attr.text + "<br>"
            elif attr.tag == "school":
                if attr.text in school_dict.keys():
                    self.school = school_dict[attr.text]
                else:
                    self.school = attr.text
            elif attr.tag == 'classes':
                self.classes = attr.text.split(', ')
            elif attr.tag == 'source':
                self.source = [attr.text]
            else:
                setattr(self, attr.tag, attr.text)
        self.text = s
        self.srd_valid = srd_list is None or self.name in srd_list

    def __str__(self):
        return self.name

    def copy(self):
        return copy.deepcopy(self)

    def append_source(self, source):
        self.source.append(source)

    def append_classes(self, entry):
        for cls in entry.classes:
            if cls not in self.classes:
                self.classes.append(cls)

    def append_spell(self, entry):
        attr_list = ["level", "school", "ritual", "time", "range", "components",
                     "duration", "text"]
        for attr in attr_list:
            if not hasattr(self, attr) and hasattr(entry, attr):
                setattr(self, attr, getattr(entry, attr))
        self.append_classes(entry)

    def __str__(self):
        return "Spell"

class Spell35(Spell):
    def __init__(self, entry, idx):
        self.entry = entry
        self.index = idx
        for attr in entry:
            if False:
                pass
            else:
                setattr(self, attr.tag, attr.text)

