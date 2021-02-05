#!/usr/bin/env python3

from gi.repository import Gio
import os


class Synchronization:

    def __init__(self):
        self.synchronizeColors()

    # get current wallpaper uri
    def get_wallpaper(self):
        settings = Gio.Settings.new("org.gnome.desktop.background")
        uri = settings.get_string("picture-uri")
        return uri

    # initialize first shell colours
    def synchronizeColors(self):
        try:
            current_wallpaper = self.get_wallpaper()
            current_wallpaper_path = current_wallpaper[7:len(current_wallpaper)]
            os.system("wal --vte -i " + current_wallpaper_path + " >/dev/null 2>&1")
        except:
            print("Shell colours synchronization failed.")


if __name__ == "__main__":
    Synchronization()
