__all__ = ['Protocol', 'Component']


class Protocol(object):
    "Symbolic base class for protocols"


class Component(object):
    "Symbolic base class for components"

    def __init__(self, class_name = None):
        self._class_name = class_name
