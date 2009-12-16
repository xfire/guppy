from provider import Provider
from guppy import *

class ConcreteProvider(Provider):
    const = RequiredFeature("provider.concrete_provider.const", isInstanceOf(int))

    def getValue(self):
        return self.const
