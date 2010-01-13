#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

"""
Setup script.
"""

from distutils.core import setup

setup(
    name = 'guppy',
    version = '1.0.0',
    description = 'Dependency Injection Framework for Python',
    long_description = '',
    author = 'Alexander Bernauer',
    author_email = 'alex@copton.net',
    url = 'http://github.com/copton/guppy/',
    download_url = 'http://github.com/copton/guppy/',
    platforms = ['any'],

    license = 'GPLv2',

    package_dir = {'guppy': 'guppy'},
    packages = ['guppy'],

    classifiers = [
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'],
)
