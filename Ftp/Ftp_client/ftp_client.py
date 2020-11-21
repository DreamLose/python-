import optparse
import socket
import json
import os,sys
SUCCESS_CODE = {
    '500':'验证通过',
    '501':'验证失败',
    '802' : '文件不存在,可以上传',
    '801' : '文件已经存在',
    '800' : '文件b不完整,是否继续'
}


class ClientHandler():
    def __init__(self):
        self.op = optparse.OptionParser()
        self.op.add_option('-s','--server',dest='server')
        self.op.add_option('-P', '--Port', dest='port')
        self.op.add_option('-u', '--username', dest='username')
        self.op.add_option('-p', '--password', dest='password')
        self.options,self.args = self.op.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()
        self.mainPath = os.path.dirname(os.path.abspath(__file__))
        self.last = 0
    def verify_args(self,options,args):
        server = options.server
        port = options.port
        # username = options.username
        # password = options.password
        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit('端口号必须是0--65535')
    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,int(self.options.port)))
    # 验证登录
    def interactive(self):
        print('开始交互....')
        if self.authenticate():
            print('-----')
            # 输入文件名
            cmd_info = input('[%s]'%self.user.strip())
            cmd_list = cmd_info.split()
            if hasattr(self,cmd_list[0]):
                func = getattr(self,cmd_list[0])
                func(*cmd_list)
    # 上传文件(断点续传)
    def put(self,*cmd_list):
        # put 12.png images
        action,local_path,target_path = cmd_list
    #     路径拼接
        local_path = os.path.join(self.mainPath,local_path)
        file_name =os.path.basename(local_path)
        file_size = os.stat(local_path).st_size
        data = {
            'action':action,
            'file_name':file_name,
            'file_size':file_size,
            'target_path':target_path
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        is_exit = self.sock.recv(1024).decode('utf-8')
        has_send = 0
        if is_exit =='800':
            # 文件不完整
            choice = input('文件存在不完整,是否续传?[Y/N]').strip()
            if choice.upper() =='Y':
                self.sock.sendall('Y'.encode('utf-8'))
                # 设置seek
                continue_position=self.sock.recv(1024).decode('utf-8')
                has_send+=int(continue_position)

            else:
                self.sock.sendall('N'.encode('utf-8'))
        elif is_exit =='801':
            # 文件完全存在
            print(SUCCESS_CODE[is_exit])
            return

        f = open(local_path,'rb')
        f.seek(has_send)
        while has_send<file_size:
            data = f.read(1024)
            self.sock.sendall(data)
            has_send += len(data)
            self.show_progress(has_send,file_size)
        f.close()
        print('上传成功')

    def show_progress(self,has_size,total):
        rate = float(has_size)/float(total)
        rate_num = int(rate * 100)
        if self.last != rate_num:
            sys.stdout.write("%s%% %s\r" %(rate_num,'#'*rate_num))
        self.last = rate_num
    # 校验登录信息
    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username = input('username:').strip()
            password = input('password:').strip()
            return self.get_auth_result(username,password)
        return self.get_auth_result(self.options.username,self.options.password)
    # 服务器端返回结果
    def response(self):
        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        return data
    def get_auth_result(self,username,pwd):
        #组织数据
        data = {
            'action':'auth',
            'username':username,
            'pwd':pwd
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        res = self.response()
        print('服务器端返回-->', res)
        if res['state_code'] == '500':

            self.user = username
            return True
        else:
            print(SUCCESS_CODE[res['state_code']])

    def ls(self):
        data = {
            'action':'ls',
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.response()
        print('服务器返回-->',data)


ch = ClientHandler()
ch.interactive()

