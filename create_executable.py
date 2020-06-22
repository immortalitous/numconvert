import os
import PyInstaller.__main__

PyInstaller.__main__.run([
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
