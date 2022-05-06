from distutils.core import setup
import zipfile
import py2exe
from tkinter import *
from ctypes import windll
setup(zipfile=None,
    options={"py2exe": {"bundle_files": 1}},
    windows=["calculadora.py"])