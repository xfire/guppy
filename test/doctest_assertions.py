#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

"""
    test hasAttributes()
    ---------------------

    >>> from guppy import hasAttributes

    >>> class Foo(object):
    ...     def __init__(self):
    ...         self.a = 23
    ...         self.b = 42

    >>> hasAttributes('a')(Foo())
    True
    >>> hasAttributes('b')(Foo())
    True
    >>> hasAttributes('a', 'b')(Foo())
    True

    >>> hasAttributes('c')(Foo())
    False

"""

"""
    test hasMethods()
    -----------------

    >>> from guppy import hasMethods

    >>> class Bar(object):
    ...     def a(self): return 23
    ...     def b(self): return 42

    >>> hasMethods('a')(Bar())
    True
    >>> hasMethods('b')(Bar())
    True
    >>> hasMethods('b', 'a')(Bar())
    True

    >>> hasMethods('c')(Bar())
    False

"""

"""
    test isInstanceOf()
    -------------------

    >>> from guppy import isInstanceOf

    >>> class BA(object): pass
    >>> class BB(object): pass
    >>> class C(BA, BB): pass

    >>> isInstanceOf(str)("test")
    True
    >>> isInstanceOf(list)([1,2,3])
    True
    >>> isInstanceOf(dict)(dict(a = 23))
    True
    >>> isInstanceOf(BA, BB, C)(C())
    True

    >>> isInstanceOf(int)("test")
    False
    >>> isInstanceOf(list)("test")
    False
    >>> isInstanceOf(BB, C)(BA())
    False

"""

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
