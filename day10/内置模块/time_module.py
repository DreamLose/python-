import time
"""
# 时间戳  用来计算
print(time.time())  # 1970 到现在的秒数
# 结构化时间
print(time.localtime()) ## time.struct_time(tm_year=2020, tm_mon=11, tm_mday=14, tm_hour=17, tm_min=2, tm_sec=50, tm_wday=5, tm_yday=319, tm_isdst=0)
t = time.localtime()
print(t.tm_year)
print(t.tm_wday) # 周几，周一为0
"""
print(time.gmtime())