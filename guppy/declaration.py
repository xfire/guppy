#
# vim:syntax=python:sw=4:ts=4:expandtab

from guppy.assertion import NoAssertion
from guppy.broker import features

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
