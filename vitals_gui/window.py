#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from headerbar import Headerbar
from stack import Stack

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        self.hbar = Headerbar(self)
        self.set_titlebar(self.hbar)

        self.stack = Stack(self)
        self.add(self.stack)

        self.screen = Gdk.Screen.get_default()
