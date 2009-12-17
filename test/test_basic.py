import unittest
import guppy

class TestBasics(unittest.TestCase):

    def test_simple(self):
        guppy.features.Provide('constant', 23)

        class Consumer(object):
            theTruth = guppy.RequiredFeature('constant', guppy.isInstanceOf(int))

        consumer = Consumer()
        self.assertEqual(consumer.theTruth, 23)


    def test_lifestyle(self):

        class Component(object):
            def __init__(self, param):
                self.param = param

        guppy.features.Provide('singleton', Component(23))
        guppy.features.Provide('transient', Component, 42)

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
