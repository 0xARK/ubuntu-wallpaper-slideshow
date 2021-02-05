#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler

import subprocess
import signal
import re
import os

# configuration variables
# edit these variables to match with your needs
# use only absolute path

wallpapers_path = "/home/mateo/Images/Wallpapers"
seconds_interval = 0
minutes_interval = 0
hours_interval = 1


class Scheduler:

    def __init__(self, cl_args):
        self.check_args(cl_args)

    # check used arguments
    def check_args(self, cl_args):
        if cl_args is not None:
            if cl_args.restart:
                self.reload_scheduler()
            elif cl_args.use:
                self.use(cl_args.use)
            elif cl_args.change:
                self.change_wallpaper()
            elif cl_args.stop:
                self.kill_scheduler()
        else:
            self.initialization()

    # automated start of the scheduler, processed by the bashrc code when a new terminal is open
    def initialization(self):
        self.change_wallpaper()
        self.schedule()

    def use(self, file):
        os.system("wal --vte -i " + wallpapers_path + "/" + file + " >/dev/null 2>&1")

    # scheduler function
    def change_wallpaper(self):
        os.system("file=$(ls " + wallpapers_path + " | shuf -n 1) && wal --vte -i " + wallpapers_path + "/$file >/dev/null 2>&1")

    # scheduler handler
    def schedule(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.change_wallpaper, 'interval', seconds=seconds_interval, minutes=minutes_interval,
                          hours=hours_interval)
        scheduler.start()

    # stop current scheduler process and start new process
    def reload_scheduler(self):
        self.kill_scheduler()
        os.system("nohup python3 wallpaper_scheduler.py >/dev/null 2>&1 &")
        print("Parameters reloaded")
        print("UWS (re)started")

    # kill current scheduler process
    def kill_scheduler(self):
        proc_ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
        proc_grep = subprocess.Popen(['grep', 'python'], stdin=proc_ps.stdout,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc_ps.stdout.close()
        out, err = proc_grep.communicate()
        found = False
        for line in out.decode("utf-8").splitlines():
            if "wallpaper_scheduler" in line:
                found = True
                pid = int(re.split(' +', line)[1])
                os.kill(pid, signal.SIGKILL)
                print("Scheduler process stopped")
        if not found:
            print("No scheduler process found")


if __name__ == "__main__":
    Scheduler(None)
