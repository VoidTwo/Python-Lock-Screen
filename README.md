# Python Lock Screen
Lightweight and power efficient lock screen / screen saver written in Python.

## Info
**Python Lock Screen** is useful if you want to lock your keyboard & mouse and save power while away from your device. Maybe you have pets or toddlers that like to mash keys and you would like to prevent that. **Python Lock Screen** is a simple Python program that makes your entire screen black and locks keyboard & mouse input until a certain combination of keys are pressed.

Default unlock keys:  
`LCTRL` + `LALT` + `RALT` + `RCTRL`

## Setup
**1.** Download the latest release or clone the repository and open a terminal in that directory

**2.** Install the required dependencies:  
- (OPTIONAL) Setup a virtual environment
- `[PYTHON] -m pip install -r requirements.txt`

## Usage
Basic:  
`[PYTHON] main.py`

Optimized:  
`[PYTHON] -OO main.py`

Advanced:  
`[PYTHONW] -OO main.py`

## Notes
`[PYTHON]` refers to your Python command or executable. For example, in Windows the Python command is usually `py`, and in some Linux distributions this might be `python3` or `python3.11`. This can also be the path to the executable; for example, in Windows it would be the path to `python.exe`.

`[PYTHONW]` refers to the Windows `pythonw.exe` executable which disables things like command line output for slightly better performance.