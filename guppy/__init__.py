#
# vim:syntax=python:sw=4:ts=4:expandtab

"""
inversion of control pseudo container based on:
    http://code.activestate.com/recipes/413268/
"""


import types
import inspect


class FeatureBroker:

    def __init__(self, allowReplace=False):
        self.providers = {}
        self.allowReplace = allowReplace

    def Provide(self, feature, provider, *args, **kwargs):
        if not self.allowReplace:
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


def NoAssertion(obj):
    return True


def isInstanceOf(*classes):
    return lambda obj : isinstance(obj, classes)


def hasAttributes(*attributes):

    def test(obj):
        for each in attributes:
            if not hasattr(obj, each): return False
        return True
    return test


def hasMethods(*methods):

    def test(obj):
        for each in methods:
            try:
                attr = getattr(obj, each)
            except AttributeError:
                return False
            if not callable(attr): return False
        return True
    return test


def implementProtocol(protocols):
    if not isinstance(protocols, (types.TupleType, types.ListType)):
        protocols = [protocols]

    def test(obj):
        for protocol in protocols:
            for fname in [n for n, f in inspect.getmembers(protocol) if callable(f)]:
                func = getattr(obj, fname, None)
                if not callable(func):
                    return False
        return True
    return test


class RequiredFeature(object):

    def __init__(self, feature, assertion = NoAssertion):
        self.feature = feature
        self.assertion = assertion

    def __get__(self, obj, T):
        return self.request()

    def get(self):
        return self.request()

    def request(self):
        obj = features[self.feature]
        assert self.assertion(obj), \
                "The value %r of %r does not match the specified criteria" \
                % (obj, self.feature)
        return obj


class Protocol(object):
    "Symbolic base class for protocols"


class Component(object):
    "Symbolic base class for components"
