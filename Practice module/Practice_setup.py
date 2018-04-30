import cx_Freeze
import sys
import matplotlib
import os.path

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Practice.py", base=base, icon="clienticon.ico")]

os.environ['TCL_LIBRARY'] = r'D:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Program Files\Python36\tcl\tk8.6'

cx_Freeze.setup(
    name = "Fingerspelling",
    options = {"build_exe": {"packages":["tkinter","matplotlib","numpy","cv2","PIL"], "include_files":["clienticon.ico", "tcl86t.dll", "tk86t.dll", "web_parallax.jpg"]}},
    version = "0.01",
    description = "Practice Indian Sign Language Gestures",
    executables = executables
    )