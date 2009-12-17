#
# vim:syntax=python:sw=4:ts=4:expandtab

import types
import inspect

__all__ = ['NoAssertion',
           'isInstanceOf',
           'hasAttributes',
           'hasMethods',
           'implementProtocol']


def NoAssertion(obj):
    return True


def isInstanceOf(*classes):
    return lambda obj: isinstance(obj, classes)


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
            for fname in [n for n, f in inspect.getmembers(protocol)
                          if callable(f)]:
                func = getattr(obj, fname, None)
                if not callable(func):
                    return False
        return True
    return test
