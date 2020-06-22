import os
import PyInstaller.__main__
print(os.path.join('resource', 'path', '*.png'))
PyInstaller.__main__.run([
    "--name=numconvert",
    "--onefile",
    "--windowed",
    "--add-data=error.png;.",
    "--add-data=share_tech_mono.ttf;.",
    # "--icon=%s" % os.path.join("resource", "path", "icon.ico"),
    "numconvert.py"
])
