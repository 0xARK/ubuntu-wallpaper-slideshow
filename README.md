
Ubuntu wallpaper slideshow
==

**Version 1.0.0**

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
On the last step, add this code on you're `~/.bashrc` file :
```bash
if pgrep -f "wallpaper_scheduler.py" &>/dev/null; then
    python3 /absolute/path/to/your/ubuntu-wallpaper-slideshow/folder/synchronize_terminal.py
else
    nohup python3 /absolute/path/to/your/ubuntu-wallpaper-slideshow/folder/wallpaper_scheduler.py &
fi
```

## Contributors

- If you want to contribute to this project, you're welcome.