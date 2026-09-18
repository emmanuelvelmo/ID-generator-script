from cx_Freeze import setup, Executable

setup(name="ID generator", executables=[Executable("ID generator script.py")], options={"build_exe": {"excludes": ["tkinter"]}})