not_srd = """
<!DOCTYPE html>
    <html>
    <head>
    <style>
    .name {
        font-size:225%;
        font-family:Georgia, serif;
        font-variant:small-caps;
        font-weight:bold;
        color:#A73335;
    </style>
    </head>
    <body>
    <div contenteditable="false"  style="width:310px; font-family:Arial,Helvetica,sans-serif;font-size:17px;">
    <div class="name"> $name is not SRD :( </div>
"""


class BaseListableEntry:
    def __init__(self, **kwargs):
        self._attributes = kwargs

    def get_attributes(self) -> dict:
        return self._attributes

    def get_name(self):
        if "name" not in self._attributes:
            raise AttributeError(f"No name attribute found in {self._attributes}!")
        return self._attributes["name"]

    def get_description(self):
        if "description" not in self._attributes:
            raise AttributeError(f"No description attribute found in {self._attributes}!")
        return self._attributes["description"]

    def get(self, key, default=None):
        return self._attributes.get(key, default)

    def is_srd_valid(self):
        return True

    def to_html(self):
        raise NotImplementedError
