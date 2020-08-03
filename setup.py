from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {}
if sys.platform == "win32":
    options["include_msvcr"] = True

setup(
    name="MD5Calc",  # Titre de l'application
    version="0.1.0",
    description="Petit utilitaire pour calculer des MD5",
    executables=[
        Executable("tkinter_md5.py", base=base),
    ],
    options={
        "build_exe": options
    },
)
