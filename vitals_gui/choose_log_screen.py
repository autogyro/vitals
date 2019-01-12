#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gtk_helper import *


class ChooseLogScreen(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        set_default_margins(self)

        self.bar_color = PRIMARY_COLOR

        self.parent = parent

        self.add(create_title("Choose log file"))

        self.choose_file_section = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.choose_file_button = Gtk.Button("Choose Log")
        self.choose_file_button.connect("clicked", self.on_file_clicked)
        self.choose_file_section.add(self.choose_file_button)

        self.path_label = create_label("")
        self.choose_file_section.add(self.path_label)

        self.add(self.choose_file_section)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self.parent.parent,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        filter_any = Gtk.FileFilter()
        filter_any.set_name("CSV files")
        filter_any.add_pattern("*.csv")
        dialog.add_filter(filter_any)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.path_label.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            self.path_label.set_text("")

        dialog.destroy()
