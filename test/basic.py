import unittest
import guppy

class TestBasics(unittest.TestCase):
    def setUp(self):
        guppy.features.Provide('constant', 23)

    def testBasics(self):
        class Consumer(object):
            theTruth = guppy.RequiredFeature('constant', guppy.isInstanceOf(int))

            
        consumer = Consumer()
        self.assertEqual(consumer.theTruth, 23)

if __name__ == '__main__':
    unittest.main()
