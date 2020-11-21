import socketserver
import json
import configparser
from conf import setting
import os
SUCCESS_CODE = {
    '500':'验证通过',
    '501':'验证失败',
    '802' : '文件不存在,可以上传',
    '801' : '文件已经存在',
    '800' : '文件b不完整,是否继续'
}

class ServerHandle(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            data = json.loads(data.decode('utf-8'))
            """
            {'action':'auth,
            'username:'yuan,
            'pwd':'123}
            """
            if not data.get('action'):print('Invalid cmd')
            if hasattr(self,data.get('action')):
                func = getattr(self,data.get('action'))
                func(**data)
            else:
                print('Invalid cmd')
    def send_response(self,state_code):
        response = {'state_code':state_code,
                    'state_mas':SUCCESS_CODE[state_code]
                    }
        self.request.sendall(json.dumps(response).encode('utf-8'))

    def auth(self,**data):
        print('服务器端收到的信息-->',data)
        username = data['username']
        pwd = data['pwd']
        user = self.authenticate(username,pwd)
        if user:
            self.send_response('500')
        else:
            self.send_response('501')

    def authenticate(self,user,pwd):
        self.user = user
        # 拼接自己的路径
        self.mainPath = os.path.join(setting.BASE_DIR, 'home', self.user)
        print('通过验证')
        return user
        # cfg = configparser.ConfigParser()
        # cfg.read(setting.ACCOUNT_PATH)
        # if user in cfg.sections():
        #    if cfg[user]['Password'] == pwd:
        #        self.user = user
        #        # 拼接自己的路径
        #        self.mainPath = os.path.join(setting.BASE_DIR,'home',self.user)
        #        print('通过验证')
        #        return user

    def put(self,**data):
        print('接收到客户端的文件数据-->',data)
        file_name = data.get('file_name')
        file_size = data.get('file_size')
        target_path = data.get('target_path')
        # 上传文件的路径
        abs_path = os.path.join(self.mainPath,target_path,file_name)


        ###############################################
        """
        判断服务器是否有这个文件,如果没有,上传,如果有,判断文件大小是否跟上传的大小一致,如果
        一致,返回已经上传,如果大小不一致,返回用户是否需要续传
        """
        has_received = 0
        # 判断上传的文件是否存在
        if os.path.exists(abs_path):
            # 文件存在,比对大小
            file_has_size = os.stat(abs_path).st_size
            if file_has_size < file_size:
                #'断点续传' N 覆盖 Y 续传
                self.request.sendall('800'.encode('utf-8'))
                choice = self.request.recv(1024).decode('utf-8')
                if choice.upper() =='Y':
                    self.request.sendall(str(file_has_size).encode('utf-8'))
                    has_received += file_has_size
                    f = open(abs_path,'ab')
                else:
                   f = open(abs_path, 'wb')
            else:
            #     文件完全存在,不需要写文件
                self.request.sendall('801'.encode('utf-8'))

                return
        else:
            self.request.sendall('802'.encode('utf-8'))
            f = open(abs_path, 'wb')
        # 写文件
        while has_received < file_size:
            data = self.request.recv(1024)
            if not data:break
            f.write(data)
            has_received +=len(data)

        f.close()

    def ls(self,**data):
        cmd =