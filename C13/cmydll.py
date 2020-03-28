"""通过ctypes模块调用C语言开发的库函数
"""
import os
from ctypes import CDLL
cdll = CDLL(os.path.abspath("cLib.dll"))
result = cdll.accum(500)
print(result)
