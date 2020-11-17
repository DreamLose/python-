"""
以字符串的形式导入模块
"""
# 方式1
# module = __import__('m1.test')  # <module 'm1' from '/Users/a2020/Desktop/gitProject/python-/Day11/m1> 拿到的是M1路径
# print(module)
# module.test.test()

# 方式二

import importlib
module = importlib.import_module('m1.test')
print(module)
module.test()

