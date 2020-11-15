# 日志
import logging

"""
format参数：
%(name)s    ：Logger的名字
%(levelno)s ：数字形式的日志级别
%(levelname)s ：文本形式的日志级别
%(pathname)s ：调用日志输出函数的模块的完整路径名，可能没有
%(fielname)s ：调用日志输出函数的模块文件名
%(module)s :调用日志输出韩式的模块名
%(funcName)s：调用日志输出函数的函数名
%(lineno)d ：调用日志输出函数的语句所在代码行
%(created)f ：当前时间，用UNIX标准的标示时间的浮点数标示
%(relativeCreated)d ：输出日志信息时的，自logger创建以来的毫秒数
%(asctime)s ： 字符串形式的当前时间，默认格式是 2020-11-15 15:50:43,608，逗号后面是毫秒
%(thread)d ： 线程ID，可能无
%(threadName)s ：线程名，可能无
%(process)d ：进程ID， 可能无
%(message)s ： 用户输出信息
"""

"""
logging.basicConfig(
    level= logging.DEBUG, # 设置告警级别，默认是 warning
    filename = "logger.log",# 设置文件路径
    filemode= "w", # 更改文件模式 r w
# 设置时间 asctime :2020-11-15 15:50:43,608 lineno:打印日志的代码行号  message:日志信 filename:代码文件名称
    format= "%(asctime)s %(filename)s[line：%(lineno)d] %(message)s",
    # datefmt= "%Y-"

)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
"""

# 通过logger对象
"""
# -------------------------创建logger
# logger = logging.getLogger()
# fh =logging.FileHandler("logger_new.log") # 向文件中发送日志
# ch = logging.StreamHandler() # 向屏幕发送日志
# #设置输出格式
# fm = logging.Formatter("%(asctime)s %(filename)s[line：%(lineno)d] %(message)s")
# fh.setFormatter(fm)
# ch.setFormatter(fm)
#
# logger.addHandler(fh)
# logger.addHandler(ch)

def logger():
    logger = logging.getLogger()
    fh = logging.FileHandler("logger_new.log")  # 向文件中发送日志
    ch = logging.StreamHandler()  # 向屏幕发送日志
    # 设置输出格式
    fm = logging.Formatter("%(asctime)s %(filename)s[line：%(lineno)d] %(message)s")
    fh.setFormatter(fm)
    ch.setFormatter(fm)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
# -------------------------设置logger
logger = logger()
# logger.level = logging.DEBUG # 设置日志级别，默认 warning
logger.setLevel("DEBUG")
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
"""

# 示例
# mylogger 相同的名字，创建的是一个对象
# 创建子对象的时候，如果父辈有打印，子对象会打印两次
# mylogger.son  创建mylogger 的子对象

logger = logging.getLogger()

logger1 = logging.getLogger("mylogger")
logger1.setLevel(logging.DEBUG)

# logger2 = logging.getLogger("mylogger")
# logger2.setLevel(logging.INFO)

fh = logging.FileHandler("loggerNew.log")  # 向文件中发送日志
ch = logging.StreamHandler()  # 向屏幕发送日志
# 设置输出格式
fm = logging.Formatter("%(name)s %(asctime)s %(filename)s[line：%(lineno)d] %(message)s")
fh.setFormatter(fm)
ch.setFormatter(fm)

logger.addHandler(fh)
logger.addHandler(ch)

logger1.addHandler(fh)
logger1.addHandler(ch)

# logger2.addHandler(fh)
# logger2.addHandler(ch)

logger.debug("logger debug message")
logger.info("logger info message")
logger.warning("logger warning message")
logger.error("logger error message")
logger.critical("logger critical message")

logger1.debug("logger1 debug message")
logger1.info("logger1 info message")
logger1.warning("logger1 warning message")
logger1.error("logger1 error message")
logger1.critical("logger1 critical message")

# logger2.debug("logger2 debug message")
# logger2.info("logger2 info message")
# logger2.warning("logger2 warning message")
# logger2.error("logger2 error message")
# logger2.critical("logger2 critical message")

