import os
import PyInstaller.__main__

PyInstaller.__main__.run([
    "--name=numconvert",
    "--onefile",
    "--windowed",
    "--add-data=error.png;.",
    "--add-data=share_tech_mono.ttf;.",
    "--add-data=icon.ico;.",
    "--icon=icon.ico",
    "numconvert.py"
])
