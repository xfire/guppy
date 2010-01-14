#
# vim:syntax=python:sw=4:ts=4:expandtab

import guppy

class Application(guppy.Component):

   con   = guppy.RequiredFeature('Console', guppy.hasMethods('write_line'))
   title = guppy.RequiredFeature('AppTitle', guppy.isInstanceOf(str))
   user  = guppy.RequiredFeature('CurrentUser', guppy.isInstanceOf(str))

   def __init__(self):
      self.x = 0

   def print_yourself(self):
      self.con.write_line('-- application instance --')
      self.con.write_line('title: %s' % self.title)
      self.con.write_line('user: %s' % self.user)
      self.con.write_line('x: %d' % self.x)
