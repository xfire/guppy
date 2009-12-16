#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

"""
    test implementProtocol()
    ------------------------

    >>> from guppy import implementProtocol, Protocol

    >>> class FooBarProtocol(Protocol):
    ...     def foo(): pass
    ...     def bar(): pass

    >>> class SpamEggsProtocol(Protocol):
    ...     def spam(): pass
    ...     def eggs(): pass

    >>> class AllProtocol(FooBarProtocol, SpamEggsProtocol): pass

    >>> class FooBar(object):
    ...     def foo(): pass
    ...     def bar(): pass

    >>> class SpamEggs(object):
    ...     def spam(): pass
    ...     def eggs(): pass

    >>> class AllInherit(FooBar, SpamEggs): pass

    >>> class All(object):
    ...     def foo(): pass
    ...     def bar(): pass
    ...     def spam(): pass
    ...     def eggs(): pass


    >>> implementProtocol(FooBarProtocol)(FooBar())
    True
    >>> implementProtocol(SpamEggsProtocol)(FooBar())
    False
    >>> implementProtocol(AllProtocol)(FooBar())
    False

    >>> implementProtocol(SpamEggsProtocol)(SpamEggs())
    True
    >>> implementProtocol(FooBarProtocol)(SpamEggs())
    False
    >>> implementProtocol(AllProtocol)(SpamEggs())
    False

    >>> implementProtocol(SpamEggsProtocol)(All())
    True
    >>> implementProtocol(FooBarProtocol)(All())
    True
    >>> implementProtocol((SpamEggsProtocol, FooBarProtocol))(All())
    True
    >>> implementProtocol(AllProtocol)(All())
    True

    >>> implementProtocol(SpamEggsProtocol)(AllInherit())
    True
    >>> implementProtocol(FooBarProtocol)(AllInherit())
    True
    >>> implementProtocol((SpamEggsProtocol, FooBarProtocol))(AllInherit())
    True
    >>> implementProtocol(AllProtocol)(AllInherit())
    True

    >>> implementProtocol(SpamEggsProtocol)('')
    False
    >>> implementProtocol(FooBarProtocol)('')
    False
    >>> implementProtocol(AllProtocol)('')
    False


    >>> implementProtocol(str)('')
    True
    >>> implementProtocol(list)('')
    False

    >>> implementProtocol(list)([])
    True
    >>> implementProtocol(str)([])
    False

    >>> implementProtocol(dict)({})
    True
    >>> implementProtocol(list)({})
    False

"""
