# "1 - 2 * ( (60 - 30 + (-40 / 5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568 / 14))-(-4 * 3) / (16 - 3 * 2))"
# res= eval("1-2*((60-30+(-40/5) * (9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))")
# print(res)
# 1 去除空格，验证是否有字母，是否少括号，验证用户输入的合法性

import re

# cal_str = "1 - 2 * ( (60 - 30 + (-40 / 5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568 / 14))-(-4 * 3) / (16 - 3 * 2))"
# 去掉空格字符
def handleStr(cal_str):
    res = cal_str.replace(" ","")

    return res
# 判断用户输入的字符串是否合法
def checkStr(cal_str):
    res = re.findall("[^0-9*+\-/().]|/0+[^.]|/0\.0*[^0-9]",cal_str) # 去除特殊字符 去除被除数为0 或者0.0情况
    if bool(res):
        return False
    res = re.findall("[\(\)]",cal_str)
    if len(res) % 2 != 0:
        return  False
    # 替换不是以"(-"开头的"-"字符
    res = re.sub("-", "&", cal_str)
    cal_str = re.sub("\(&", "(-", res)
    return cal_str

def addFunc(x,y):
    return x+y
def subFunc(x,y):
    return x-y
def mluFunc(x,y):
    return x*y
def divFunc(x,y):
    return x/y

def handDate(cal_str,res,type):
    ret = re.findall("[0-9\-.]+", res)  # 提取数字
    result = 0.0
    if type == "/":
        result = divFunc(float(ret[0]), float(ret[1]))
    elif type == "*":
        result = mluFunc(float(ret[0]), float(ret[1]))
    elif type == "&":
        result = subFunc(float(ret[0]), float(ret[1]))
    elif type == "+":
        result = addFunc(float(ret[0]), float(ret[1]))
    return cal_str.replace(res, str(result))  # 替换原字符串
def cal(cal_str):
    # 去掉括号
    cal_str = re.sub("\(|\)", "", cal_str)
    while True:
        # 匹配到只有数字的时候，循环结束
        res = re.findall("[^0-9\-.]+", cal_str)
        if not res:
            return cal_str
        # 先计算乘除
        res = re.search("[0-9\-.]+/[0-9\-.]+", cal_str) # 获取除法运算
        if res:
            cal_str = handDate(cal_str,res.group(),'/')
            continue
        res = re.search("[0-9\-.]+\*[0-9\-.]+", cal_str) #获取乘法运算
        # 乘法运算
        if res:
            cal_str = handDate(cal_str, res.group(), '*')
            continue
        res = re.search("[0-9\-.]+&[0-9\-.]+", cal_str)  # 获取减法运算
        # 减法运算
        if res:
            cal_str = handDate(cal_str, res.group(), '&')
            continue
        res = re.search("[0-9\-.]+\+[0-9\-.]+", cal_str)  # 获取加法运算
        # 加法运算
        if res:
            cal_str = handDate(cal_str, res.group(), '+')
            continue
    return cal_str

cal_str = input("请输入计算的字符串：")
print("eval==",eval(cal_str))
cal_str = handleStr(cal_str)
cal_str = checkStr(cal_str)
# 输入的没有问题
if cal_str:
    #     先获取括号中的内容
    while True:
        ret = re.search("\([^()]*\)",cal_str)  #首先匹配括号
        if ret:
            res = cal(ret.group())
            cal_str = cal_str.replace(ret.group(),res)
        else:
            res = cal(cal_str)
            # 替换运算结果
            cal_str = cal_str.replace(cal_str, res)
            print("运算结果：",cal_str)
            break
else:
    print("输入格式错误：")
