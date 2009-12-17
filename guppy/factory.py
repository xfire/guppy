#
# vim:syntax=python:sw=4:ts=4:expandtab

from broker import features
import traceback


class Component(object):

    def __init__(self, class_name):
        self.class_name = class_name


def load_code(path):
    parts = path.split('.')
    module_name = '.'.join(parts[:-1])
    attribute_name = parts[-1]

    try:
        module = __import__(module_name, {}, {}, [attribute_name], level=0)
        return getattr(module, parts[-1])
    except ImportError, e:
        raise ImportError("failed to import '%s':\n%s" % (module_name, traceback.format_exc()))
    except AttributeError, e:
        raise ImportError("attribute '%s' not found in '%s':\n%s" % (attribute_name, module_name, traceback.format_exc()))


def create_component(class_name):
    cls = load_code(class_name)
    return cls()


def create(config):
    for key, value in config.iteritems():
        if isinstance(value, Component):
            component = create_component(value.class_name)
            features.Provide(key, component)
        else:
            features.Provide(key, value)

    return features
