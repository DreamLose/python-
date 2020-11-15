import time
# 引用多层模块

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__ )))
sys.path.append(BASE_DIR)
from 模块.module import cal
print(os.path.dirname(os.path.dirname(__file__)))
print(__file__)

print(cal.add(2,3))
