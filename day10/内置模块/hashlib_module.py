# 用于加密操作，提供了sha1，sha224，sha256，sha384，sha521，md5算法
import hashlib
# 存取密码
obj = hashlib.md5()
obj.update("hello world".encode('utf8'))

print(obj.hexdigest()) #5d41402abc4b2a76b9719d911017c592