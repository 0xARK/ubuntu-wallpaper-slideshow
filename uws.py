from wallpaper_scheduler import Scheduler as Sch

import argparse

# get command line args and write help
parser = argparse.ArgumentParser(description='UWS is a wallpaper change scheduler for ubuntu that matches the colours '
                                             'of the terminal with those of the current wallpaper.')

parser.add_argument('-c', '--change', action='store_true', help="Change the current wallpaper and terminal theme, "
                                                                "without reloading configuration parameters")
parser.add_argument('-r', '--restart', action='store_true',
                    help="Start or restart the scheduler by reloading configuration variables. Use this command when "
                         "you change one of them.")
parser.add_argument('-s', '--stop', action='store_true', help="Stop the current scheduler processus.")
parser.add_argument('-u', '--use', help="Filename of a wallpaper to use, present in the wallpaper directory.")
args = parser.parse_args()

# pass args to the scheduler
Sch(args)a
