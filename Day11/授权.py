# 授权定制,只修改部分功能(不通过继承)
import time
class Open:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        # self.filename=filename
        self.file=open(filename,mode,encoding=encoding)
        self.mode=mode
        self.encoding=encoding
    def write(self,line):
        # 写入的每行都添加时间
        t = time.strftime("%Y-%m-%d %X")
        self.file.write('%s %s' %(t,line))
    def __getattr__(self, item):
        print(item,type(item))
        # 根据传入的str 返回对应的方法
        return getattr(self.file,item)

    # def read(self):
    #     pass
    # def write(self):
    #     pass

f1 = Open('a.txt','w+')
# print(f1.file)
# f1.read
# print(f1.read)
# f1.file.read()
f1.write('121312312312 \n')
f1.write('83823888232\n')
f1.seek(0)
print(f1.read())