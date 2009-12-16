import unittest
import guppy


class Component(object):

    def __init__(self, param):
        self.param = param


class TestBasics(unittest.TestCase):

    def setUp(self):
        guppy.features.Provide('singleton', Component(23))
        guppy.features.Provide('transient', Component, 42)

    def testBasics(self):
        s = guppy.RequiredFeature('singleton', guppy.isInstanceOf(Component)).get()
        s2 = guppy.RequiredFeature('singleton', guppy.isInstanceOf(Component)).get()
        t = guppy.RequiredFeature('transient', guppy.isInstanceOf(Component)).get()
        t2 = guppy.RequiredFeature('transient', guppy.isInstanceOf(Component)).get()

        self.assertEqual(s, s2)
        self.assertNotEqual(t, t2)

        self.assertEqual(s.param, 23)
        self.assertEqual(s2.param, 23)

        self.assertEqual(t.param, 42)
        self.assertEqual(t2.param, 42)


if __name__ == '__main__':
    unittest.main()
