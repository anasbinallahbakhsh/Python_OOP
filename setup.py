import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

# Python ke tcl/tk folders (Python 3.11 ke liye, apne aap sahi path nikal leta hai)
os.environ['TCL_LIBRARY'] = os.path.join(sys.base_prefix, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(sys.base_prefix, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("238_vpad.py", base=base, icon=r"E:\icons2\icon.ico")]

# Jo files exe ke sath jayengi
include_files = [
    (r"E:\icons2", "icons2"),
]

# tcl/tk dll agar maujood hon to add kar do
for dll in ('tcl86t.dll', 'tk86t.dll'):
    dll_path = os.path.join(sys.base_prefix, 'DLLs', dll)
    if os.path.exists(dll_path):
        include_files.append(dll_path)

cx_Freeze.setup(
    name="Vpad Text Editor",
    options={"build_exe": {"packages": ["tkinter", "os"], "include_files": include_files}},
    version="0.01",
    description="Tkinter Application",
    executables=executables
)
