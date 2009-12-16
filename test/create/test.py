import unittest
from guppy import *

class TestCreate(unittest.TestCase):
    def runTest(self):
        components = create({
                "Consumer" : Component("consumer.Consumer"),
                "Provider" : Component("provider.concrete_provider.ConcreteProvider"),
                "provider.concrete_provider.const" : 23,
                        })
        
        const = components["Consumer"].run()
        self.assertEqual(const, 23)

if __name__ == "__main__":
    unittest.main()
        
