#
# vim:syntax=python:sw=4:ts=4:expandtab

import guppy


class SimpleConsole(guppy.Component):

    def write_line(self, s):
        print s


class BetterConsole(guppy.Component):

    def __init__(self, prefix = ''):
        self.prefix = prefix

    def write_line(self, s):
        lines = s.split('\n')
        for line in lines:
            if line:
                print self.prefix, line
            else:
                print self.prefix
