"""扩展模块设置"""
from distutils.core import setup, Extension
mymath = Extension('mymath', sources=['cppMymath.cpp'])
setup(ext_modules=[mymath])
