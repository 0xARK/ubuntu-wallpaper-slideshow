from apscheduler.schedulers.blocking import BlockingScheduler
from gi.repository import Gio
import os

# edit these variables to match with your needs
# use only absolute path
wallpapers_path = "/home/mateo/Images/Wallpapers"
seconds_interval = 0
minutes_interval = 0
hours_interval = 1

# get current wallpaper uri
def get_wallpaper():
    settings = Gio.Settings.new("org.gnome.desktop.background")
    uri = settings.get_string("picture-uri")
    return uri

# scheduler functions
def change_wallpaper():
    os.system("file=$(ls " + wallpapers_path + " | shuf -n 1) && wal --vte -i " + wallpapers_path + "/$file")

# initialize first shell colours
try:
	change_wallpaper()
	current_wallpaper = get_wallpaper()
	current_wallpaper_path = current_wallpaper[7:len(current_wallpaper)]
	os.system("wal --vte -i " + current_wallpaper_path)
except:
	print("Shell colours synchronization failed.")

# scheduler setup
scheduler = BlockingScheduler()
scheduler.add_job(change_wallpaper, 'interval', seconds=seconds_interval, minutes=minutes_interval, hours=hours_interval)
scheduler.start()
