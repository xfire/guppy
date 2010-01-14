#!/usr/bin/env python
#
# vim:syntax=python:sw=4:ts=4:expandtab

import guppy

from app import Application
from components import get_current_user
from components.console import SimpleConsole

if __name__ == '__main__':

    # inject dependencies
    guppy.features.Provide('AppTitle', 'Inversion of Control ...\n\n... The Python Way')
    guppy.features.Provide('CurrentUser', get_current_user)
    guppy.features.Provide('Console', SimpleConsole) # <-- transient lifestyle
    # features.Provide('Console', SimpleConsole())# <-- singleton lifestyle

    # use dependencies
    app = Application()
    app.print_yourself()
