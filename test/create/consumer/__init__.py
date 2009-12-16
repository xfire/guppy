from guppy import *
import provider

class Consumer(object):
    provider = RequiredFeature("Provider", isInstanceOf(provider.Provider))

    def run(self):
        return self.provider.getValue() 
