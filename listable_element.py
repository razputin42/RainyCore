class BaseListableEntry:
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def get_attributes(self) -> dict:
        return self._attributes

    def get_name(self):
        if "name" not in self._attributes:
            raise AttributeError(f"No name attribute found in {self._attributes}!")
        return self._attributes["name"]

    def get(self, key, default=None):
        return self._attributes.get(key, default)
