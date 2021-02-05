
Ubuntu wallpaper slideshow
==

**Version 1.1.0**

**Made on February 2021**

## Description

Wallpaper slideshow for ubuntu that adapts colours of current wallpaper to the terminal

## Requirements

```bash
pip3 install pywal
pip3 install apscheduler
```

## Installation

Fisrt, you need to clone this repository :

```bash
git clone https://github.com/0xARK/ubuntu-wallpaper-slideshow
cd ubuntu-wallpaper-slideshow
```

On the next step, you have to edit `wallpaper_scheduler.py` :

```python
wallpapers_path = "/absolute/path/to/your/wallpaper/folder"
seconds_interval = 5 # number of seconds before change wallpaper
minutes_interval = 0 # number of minutes before change wallpaper
hours_interval = 0 # number of hours before change wallpaper
```
On the last step, add this code on you're `~/.bashrc` file and be sure to use the right path :
```bash
if pgrep -f "wallpaper_scheduler.py" &>/dev/null; then
    python3 /absolute/path/to/your/ubuntu-wallpaper-slideshow/folder/synchronize_terminal.py
else
    nohup python3 /absolute/path/to/your/ubuntu-wallpaper-slideshow/folder/wallpaper_scheduler.py >/dev/null 2>&1 &
fi
```
## Usage

A list of command to execute once process is running is available by typing `python3 uws.py -h` :

```
usage: uws.py [-h] [-c] [-r] [-s] [-u USE]

UWS is a wallpaper change scheduler for ubuntu that matches the colours of the
terminal with those of the current wallpaper.

optional arguments:
  -h, --help         show this help message and exit
  -c, --change       Change the current wallpaper and terminal theme, without
                     reloading configuration parameters
  -r, --restart      Start or restart the scheduler by reloading configuration
                     variables. Use this command when you change one of them.
  -s, --stop         Stop the current scheduler processus.
  -u USE, --use USE  Filename of a wallpaper to use, present in the wallpaper
                     directory.
```

## Contributors

- If you want to contribute to this project, you're welcome.