#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)
   Copyright 2017 Ian Santopietro (ian@system76.com)
   Copyright 2018 Kyle Corry (kylecorry31@gmail.com)
'''

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Headerbar(Gtk.HeaderBar):

    def __init__(self, parent):
        Gtk.HeaderBar.__init__(self)
        self.parent = parent

        self.set_show_close_button(True)
        self.set_has_subtitle(False)
