import sys
# sys.argv  # 命令行参数list，第一个元素是程序本身路径
# sys.exit(n) # 退出程序，正常退出是exit(0)
# sys.version # 获取python解释程序的版本信息
# sys.maxint # 最大int值
# sys.path # 返回模块的搜索路径，初始化时使用pythonpath环境变量的值
# sys.platform # 返回操作系统平台名称
# sys.stdout.write("#")  # 进度条
# a = input("请输入：")
# if a=='1':
#     print("a==1")
# else:
#     sys.exit(0)
# print(sys.argv)
import time
for i in range(100):
    sys.stdout.write("#")  # 进度条
    time.sleep(0.1)
    sys.stdout.flush()