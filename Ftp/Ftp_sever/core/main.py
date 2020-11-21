# 解析命令行
import optparse
import socketserver
from conf import setting
from core import handelService

class ArgvHandle():
    def __init__(self):
        self.op = optparse.OptionParser()
        # self.op.add_option('-s','--s',dest='server')
        # self.op.add_option('-P','--port', dest='port')
        options,args = self.op.parse_args()
        self.verify_args(options,args)
    def verify_args(self,options,args):
        '获取终端参数,输入的start 启动ftp服务'
        cmd = args[0]
        # 判断是否包含属性 (反射)
        if hasattr(self,cmd):
            func = getattr(self,cmd) # 获取方法
            func()
    # 启动ftp服务
    def start(self):
        print('start ftp')
        s = socketserver.ThreadingTCPServer((setting.IP,setting.PORT),handelService.ServerHandle)
        s.serve_forever()
