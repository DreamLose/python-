import pickle
dic = {'name':'alex','age':34,'sex':'male'}
print(dic)
j = pickle.dumps(dic)
print(j,type(j)) # <class 'bytes>
# f = open("pick.txt",'wb')
# f.write(j)  # 等价pickle.dump()
# f.close()
f = open("pick.txt",'rb')
data = pickle.loads(f.read())  # 等价pickle.load(f)
print(data["name"])