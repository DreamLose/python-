import os
# os.path.dirname() #文件的上一层目录
# res = os.path.dirname("/Users/a2020/Desktop/gitProject/python-/day10/内置模块/os_module.py")
# # print(os.path.dirname("/Users/a2020/Desktop/gitProject/python-/day10/内置模块/os_module.py"))
# print("dirname ==",res)
# res = os.getcwd() # 获取当前工作目录，即当前python脚本工作的目录路径
# print("getcwd ==",res)
# res = os.chdir("test") # 改变当前工作目录，相当于shell下的cd
# print("更改后的路径：",os.getcwd())
# res = os.chdir("..") # 改变当前工作目录，相当于shell下的cd
# print("更改后的路径：",os.getcwd())
# res = os.curdir("")    #返回当前目录
# print("curdir ==",res)
# os.makedirs('dirname1/dirname2') # 新建目录 可生成多层递归目录
# os.removedirs('dirname1/dirname2') # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，一次类推
# os.mkdir('dirname') # 生成单级目录，相当于shell 中的mkdir dirname
# os.rmdir('dirname') # 删除单级空目录，若目录不为空，则无法删除，报错，相当于shell中的rmdir dirname
# os.listdir('dirname') # 列出指定目录下的所有文件和子目录，包括隐藏文件，鼻翼列表方式打印
# os.remove() # 删除一个文件
# os.rename("oldname",'newname') # 重命名文件/目录
# os.stat('path/filename') # 获取文件/目录信息 (st_size ：多少字节；st_atime：用户上次访问时间 st_mtime:用户上次修改的时间 st_ctime：创建时间)
# os.sep  # 输出操作系统特定的路径分割符。win下为"\\",linux 为'/'
# os.linesep # 输出当前平台使用的终止符，win下为"\r\n", linux为"\n"
# os.pathsep #  输出用于分割文件路径的字符串，win下为";", linux为":"
# os.name # 输出字符串指示当前使用平台，win为"nt", linux为"posix"
# os.system('bash command') # 运行的shell命令，直接显示
# os.environ #获取系统环境变量
# os.path.abspath(path) #返回path规范化的绝对路径
# os.path.split(path) #将path分割成目录文件和文件名二元组返回
# os.path.dirname(path) #返回pathu目录，其实就是os.path.split(path)的第一个元素
# os.path.basename(path) # 返回path 最后的文件名。如果path以/ 或 \ 结尾，那么返回空值
# os.path.exists(path) # 如果path存在。返回True，否则返回False
# os.path.isabs(path) # 如果path是绝对路径，返回True
# os.path.isfile(path) # 如果path是一个存在的文件，返回True
# os.path.isdir(path) # 如果path是一个存在的目录，返回True
#最重要 ##os.path.join(path1 [,path2[, ... ]]) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path) # 返回path缩指向的文件或者目录的最后存取时间
# os.path.getctime(path) # 返回path缩指向的文件或者目录的创建时间
# os.path.getmtime(path) # 返回path缩指向的文件或者目录的最后修改时间
# os.path.getsize(path) # 返回path缩指向的文件或者目录的大小（字节）
res = os.path.split(r'/Users/a2020/Desktop/gitProject/python-/day10/内置模块/os_module.py')
print("split ==",res)
res = os.path.dirname(r"/Users/a2020/Desktop/gitProject/python-/day10/内置模块/os_module.py")
print("dirname ==",res)
res = os.path.basename(r"/Users/a2020/Desktop/gitProject/python-/day10/内置模块/os_module.py")
print("basename ==",res)

a = "/Users/a2020"
b = "Desktop/gitProject"
c = 'python-/day10/内置模块'
res = os.path.join(a,b,c) # 路径拼接 直接用字符串 "+" 拼接的话 不同的操作系统拼接符不同
print("join ==",res)
print(os.environ)

