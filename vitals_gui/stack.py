#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)
   Copyright 2017 Ian Santopietro (ian@system76.com)
   Copyright 2018 Kyle Corry (kylecorry31@gmail.com)
'''

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from choose_log_screen import ChooseLogScreen

class Stack(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.parent = parent

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(300)

        self.choose_log_screen = ChooseLogScreen(self)

        self.stack.add_titled(self.choose_log_screen, "choose_log_screen", "Choose Log File")

        self.pack_start(self.stack, True, True, 0)
