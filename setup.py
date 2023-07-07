from cx_Freeze import setup, Executable

setup(
    name="DPC Frame Maker",
    version="0.0.1",
    description="DPC Frame Maker Made By Churitoring",
    executables=[Executable("dfmc.py", icon="dfmc.ico")]
)
