#
# vim:syntax=python:sw=4:ts=4:expandtab


class FeatureBroker:

    def __init__(self):
        self.providers = {}

    def Provide(self, feature, provider, *args, **kwargs):
        assert not feature in self.providers, \
                "Duplicate feature: %r" % feature
        if callable(provider):
            call = lambda: provider(*args, **kwargs)
        else:
            call = lambda: provider
        self.providers[feature] = call

    def __getitem__(self, feature):
        try:
            provider = self.providers[feature]
        except KeyError:
            raise KeyError("Unknown feature named %r" % feature)
        return provider()


features = FeatureBroker()
