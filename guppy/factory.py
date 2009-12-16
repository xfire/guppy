#
# vim:syntax=python:sw=4:ts=4:expandtab

from broker import features


class Component(object):

    def __init__(self, class_name):
        self.class_name = class_name


def load_code(path):
    parts = path.split('.')
    try:
        module = '.'.join(parts[:-1])
        module = __import__(module, {}, {}, module)
        return getattr(module, parts[-1])
    except ImportError, e:
        raise ImportError('module not found: %s (%s)' %
                          ('.'.join(parts[:-1]), e))
    except AttributeError, e:
        raise ImportError('not found: %s (%s)' % (parts[-1], e))


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
