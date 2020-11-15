import time
"""
# 时间戳  用来计算
print(time.time())  # 1970 到现在的秒数
# 结构化时间
print(time.localtime()) ## time.struct_time(tm_year=2020, tm_mon=11, tm_mday=14, tm_hour=17, tm_min=2, tm_sec=50, tm_wday=5, tm_yday=319, tm_isdst=0)
t = time.localtime()
print(t.tm_year)
print(t.tm_wday) # 周几，周一为0

# ---结构化时间---世界标准时间（UTC）
print(time.gmtime())
# 将结构化时间 ===》时间戳  mktime
print(time.mktime(time.localtime()))

# 将结构化时间转换成字符串时间 strftime
# Y-m-d
# %H --- 代表时分秒
print(time.strftime("%Y-%m-%d %X",time.localtime()))
# 字符串时间 === 》 结构化时间
print(time.strptime("2020-11-14 17:16:11","%Y-%m-%d %X"))

# 把一个结构化时间转换成固定的字符串格式，不需要自己定义
Sat Nov 14 17:21:32 2020
print(time.asctime())
#把一个时间戳转换成固定的字符串格式，不需要自己定义
Sat Nov 14 17:21:32 2020
print(time.ctime())

#线程推迟
sleep() 
"""

import datetime
print(datetime.datetime.now())

