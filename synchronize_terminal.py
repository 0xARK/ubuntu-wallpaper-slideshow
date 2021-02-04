from gi.repository import Gio
import os

# get current wallpaper uri
def get_wallpaper():
    settings = Gio.Settings.new("org.gnome.desktop.background")
    uri = settings.get_string("picture-uri")
    return uri

# initialize first shell colours
try:
    current_wallpaper = get_wallpaper()
    current_wallpaper_path = current_wallpaper[7:len(current_wallpaper)]
    os.system("wal --vte -i " + current_wallpaper_path)
except:
    print("Shell colours synchronization failed.")
