# 字符串 =》 转换
a = '1212'
print(type(a))
b = int(a)
b += 100
print(b)
print(type(b))
print("----------")
num = "001111111"
c = int(num, base=10)
print(c)
print("----------")
# 数字二进制的位数，至少用n位
print(c.bit_length())
print("----------")


















