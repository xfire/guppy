#
# vim:syntax=python:sw=4:ts=4:expandtab

import os

def get_current_user():
    return os.getenv('USERNAME') or 'unknown'
