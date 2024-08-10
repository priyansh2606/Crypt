import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "C:\Users\Asus\Desktop\HTML VS CODES\Crypt-master\Crypt.py/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "C:\Users\Asus\Desktop\HTML VS CODES\Crypt-master\Crypt.py/tcl/tk8.6"

base = None
include_files = [
    "./assets",
    "C:\Users\Asus\Desktop\HTML VS CODES\Crypt-master\Crypt.py/DLLs/tcl86t.dll",
    "C:\Users\Asus\Desktop\HTML VS CODES\Crypt-master\Crypt.py/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Crypt",
    version="1.0",
    description="Encryption and Decryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "Crypt.py",
            base=base,
            targetName="Crypt.exe",
            icon="./assets/icon.ico"
        )
    ]
)
