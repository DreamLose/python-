try:
    age = input(">>>:")
    int(age)  #主逻辑
    name = input(">>>:")
    int(name) #主逻辑
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print('------------')
# 万能异常
except Exception as e:
    print('==========>',e)
else:
    print("try 内代码块没有异常")
finally:
    print("无论异常与否,都会执行")
print("++++++++++++++=")