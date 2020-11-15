# dic = '{"name":"alex"}'
# with open("json.txt",'w') as f_write:
#     f_write.write(dic)
# with open("json.txt",'r') as f_read:
#     data = f_read.read()
#     print(data)
import json
dic = {"name":"alex"}
res = json.dumps(dic) # 字典====》jsonStr
with open("json.txt",'r') as f_read:
    data = json.loads(f_read.read()) # jsonStr==>dic
    print(data,type(data))
    print(data["name"])
# print(res,type(res))
# res = json.dumps(8)
# print(res,type(res))
# res = json.dumps('hello')
# print(res,type(res))
# res = json.dumps([1,2,3])
# print(res,type(res))
# with open("json.txt",'w') as f_write:
#     f_write.write(res)
# dict = {"name":"alex","age":13}
# f = open("json1.txt","w")
# json.dump(dict,f)
# f.close()
f = open("json1.txt","r")
data = json.load(f)  #定制化，用于文件操作，局限性
f.close()
print(data,type(data))

