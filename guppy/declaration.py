#
# vim:syntax=python:sw=4:ts=4:expandtab

from guppy.assertion import NoAssertion
from guppy.broker import features

class RequiredFeature(object):

    def __init__(self, feature, assertion = NoAssertion):
        self.feature = feature
        self.assertion = assertion
        self.cache = None

    def __get__(self, obj, T):
        return self._get()

    def get(self):
        return self._get()

    def _get(self):
        if self.cache == None:
            self.cache = self._request()
        return self.cache

    def _request(self):
        obj = features[self.feature]
        assert self.assertion(obj), \
                "The value %r of %r does not match the specified criteria" \
                % (obj, self.feature)
        return obj
