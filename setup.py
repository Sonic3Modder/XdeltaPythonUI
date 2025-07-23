from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [],
    "include_files": ["xdelta3.exe"],  # <- include it
}

setup(
    name="XdeltaUIPython",
    version="1.0",
    description="Xdelta Patch GUI",
    options={"build_exe": build_exe_options},
    executables=[Executable("xdeltapatcherpython.py")],
    icons=["icon.ico"],
)
