class Settings:
    options = None

    @classmethod
    def getSetting(cls, key):
        cls.loadSettings()
        return cls.options[key]

    @classmethod
    def loadSettings(cls):
        if cls.options is not None:
            return
        with open('.env', 'r') as env:
            for line in env:
                eq_index = line.index('=')
                cls.options[line[:eq_index]] = line[eq_index+1:]
