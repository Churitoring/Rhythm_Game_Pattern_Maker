#python setup.py build
from cx_Freeze import setup, Executable 

setup(
    name="Rhythm Game Pattern Maker",
    version="0.0.1",
    description="Rhythm Game Pattern Maker By Churitoring",
    executables=[Executable("RGPM.py", icon="RGPM.ico")]
)
