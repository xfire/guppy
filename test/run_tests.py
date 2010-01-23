#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

import os
import sys
import glob
import unittest
import doctest

# setup project
src_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.realpath(os.path.join(src_path, '..'))
sys.path.insert(0, src_path)


def get_path(dirname):
    op = os.path
    return op.join(op.realpath(op.dirname(__file__)), dirname)

suite = unittest.TestSuite()

for f in glob.glob('doctest*.py'):
    suite.addTest(doctest.DocFileSuite(f))

for f in glob.glob('test*.py'):
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(f[:-3]))

for dirname in ['create']:
    path = get_path(dirname)
    sys.path.insert(0, path)
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName('.'.join((dirname, 'test'))))


unittest.TextTestRunner(verbosity = 2).run(suite)
