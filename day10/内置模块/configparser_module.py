# 写配置文件,配置文件的操作
import configparser

"""
# 创建配置文件
config = configparser.ConfigParser()
print(config)
config['DEFAULT'] = {'ServerAliveInterval':'45',
                      'Compression':'yes',
                      'CompressionLevel':'9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.sever.com'] = {}
topsecret = config['topsecret.sever.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
#
with open('example.ini','w') as configfile:
    config.write(configfile)
"""
# 增删改查
config = configparser.ConfigParser()
config.read('example.ini') # 读取配置文件
# print(config.sections()) #获取配置文件块
# print("bitbucket.org1" in config)
# print("bitbucket.org" in config)
# print("DEFAULT" in config)
# print(config['bitbucket.org']['user']) # 获取块下对应信息
# print(config['DEFAULT']['compressionlevel'])
# ============查===========
"""
# 会遍历出 DEFAULT下的键值 【DEFAULT】命名的会出现这个问题
for key in config['bitbucket.org']:
    print(key)
# 遍历 bitbucket.org 下面的 key
print(config.options('bitbucket.org'))
# 获取 bitbucket.org 下面的 键跟值
print(config.items('bitbucket.org'))
# 根据key 获取 值
print(config.get('bitbucket.org','compression'))
print(config.get('bitbucket.org','user'))
"""
# 增，改，删。结束后都要写入文件 config.write(open('','w))
# =====增=========
# 新增块
config.add_section('yuan')
# 新增块里的键值对
config.set('yuan','key','111')
# 删除
# 删除块
config.remove_section('topsecret.sever.com')
# 删除块下的键值对
config.remove_option('bitbucket.org','user')
# 这里open 没有赋值给变量，没有句柄，不需要close
config.write(open("new.cfg",'w'))