import os
import PyInstaller.__main__

if os.name == "nt":
    PyInstaller.__main__.run([
        "--clean",
        "--distpath=../bin/",
        "--workpath=../build/",
        "--name=numconvert",
        "--onefile",
        "--windowed",
        "--add-data=icon.ico;.",
        "--add-data=copy.png;.",
        "--add-data=error.png;.",
        "--add-data=share_tech_mono.ttf;.",
        "--icon=icon.ico",
        "numconvert.py"
    ])
elif os.name == "posix":
    PyInstaller.__main__.run([
        "--clean",
        "--distpath=../bin/",
        "--workpath=../build/",
        "--name=numconvert",
        "--onefile",
        "--add-data=copy.png:.",
        "--add-data=error.png:.",
        "--hidden-import=PIL.ImageTk",
        "numconvert.py"
    ])
