from json import load
from exceptions import NotDictException, ValueNotStringException, ValueNotScriptOrUrlException

class AliasDecoder:
    def __init__(self, filename):
        self.filename = filename
        self.__decode_aliases_from_file()

    def __decode_aliases_from_file(self):
        aliases = None
        with open(self.filename, 'r') as file:
            aliases = load(file)
        self.__validate_is_dict(aliases)
        self.__validate_all_values_strings(aliases)
        self.__validate_values_are_scripts_or_urls(aliases)
        self.aliases = aliases

    @staticmethod
    def __validate_is_dict(obj):
        if not isinstance(obj, dict):
            raise NotDictException('File cannot be converted to a dictionary.')

    @staticmethod
    def __validate_all_values_strings(dict):
        for key, value in dict.items():
            if not isinstance(value, str):
                raise ValueNotStringException('Value {0} for key {1} is not a string.'.format(value, key))

    @staticmethod
    def __validate_values_are_scripts_or_urls(dict):
        for key, value in dict.items():
            if value.find('$') != 0 and value.find('http://') != 0 and value.find('https://') != 0:
                raise ValueNotScriptOrUrlException('Value {0} for key {1} is not a script or url.'.format(value, key))
