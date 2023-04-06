class BaseListableEntry:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_name(self):
        if "name" not in self.attributes:
            raise AttributeError(f"No name attribute found in {self.attributes}!")
        return self.attributes["name"]

    def get(self, key, default=None):
        return self.attributes.get(key, default)
