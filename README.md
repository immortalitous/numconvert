# numconvert
Simple converter for various numeral systems (binary, octal, hexadecimal, ...).

## Content
1. [Appearance](#1-appearance)
2. [Compatibility](#2-compatibility)
3. [Downloads](#3-downloads)


## 1. Appearance
![user interface on ubuntu](img/ui_ubuntu.png)
![user interface on windows](img/ui_windows.png)


## 2. Compatibility
### Operating systems
Following operating systems are tested and supported:
- Ubuntu 20.04 LTS
- Windows 10

The binary files of the program were also frozen (Python equivalent of compiling) on these systems.

### Source code

The source code is running on Python version 3.8.<br>
Following packages, not included in the standard library, are [required](requirements.txt):
- Pillow
- pyglet
- pyperclip
- ttkthemes
- PyInstaller (used for freezing)


## 3. Downloads
- [Numconvert for Linux](bin/numconvert)
- [Numconvert for Windows](bin/numconvert.exe)

### Freezing
You can also run [create_executable.py](src/create_executable.py) to freeze the source code into a standalone executable yourself.
