import ctypes
import os
import platform
from pathlib import Path

PATH = Path(__file__).parent


def try_add_mingw_dll_dirs():
    for p in os.environ["PATH"].split(os.pathsep):
        path = Path(p)
        if (path / "libgomp-1.dll").exists():
            os.add_dll_directory(str(path))
            return


if os.name == "nt":
    try_add_mingw_dll_dirs()

if platform.system() == "Windows":

    def find_dll(x):
        return str(next(PATH.glob(x)))

    PATH_LIBDIVSUFSORT = find_dll("libdivsufsort.dll")
    PATH_LIBDIVSUFSORT64 = find_dll("libdivsufsort64.dll")
else:
    PATH_LIBDIVSUFSORT = next(PATH.glob("libdivsufsort.*"))
    PATH_LIBDIVSUFSORT64 = next(PATH.glob("libdivsufsort64.*"))

libdivsufsort = ctypes.CDLL(PATH_LIBDIVSUFSORT)
libdivsufsort64 = ctypes.CDLL(PATH_LIBDIVSUFSORT64)
