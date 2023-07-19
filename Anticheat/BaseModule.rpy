init -999 python in AntiCheat:
    # Setting Module
    class BaseSettings(object):
        def __init__(self, defaults: dict[str, Any] = None):
            self.defaults = defaults

            if not defaults:
                self.defaults = dict()

            for name in self.defaults.keys():
                setattr(self, name, self.defaults.get(name, None))


        def __setattr__(self, name, value):
            if not (name in self.defaults.keys()):
                raise InvalidSettingName("Invalid setting name: '%s'" % name)

            object.__setattr__(self, name, value)


        def __getattribute__(self, name):
            try:
                return object.__getattribute__(self, name)
            except:
                raise InvalidSettingName("Invalid setting name: '%s'" % name)


    class BaseAntiCheatModule(object):
        def __init__(self, name):
            self.name = name

        def run(self):
            raise Exception("You did not configure the anti-cheat module '%s' what to do now" % self.name)

        def check(self):
            raise Exception("You have not configured the anti-cheating module '%s' how to check whether it is cheating" % self.name)