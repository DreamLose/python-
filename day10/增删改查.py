# 增删改查
# 查询
import os
def fetch(data):
    print("查询功能")
    print("\033[1;43m用户数据是\033[0m",data)
    pass
# 增加
def add():
    print("增加功能")
    pass
# 修改
def change():
    print("修改功能")
    # 先读在写
    # os.rename("源文件","源文件.bak")
    # os.rename("修改后文件", "源文件")
    # os.remove('源文件.bak')
    pass
# 删除
def delete():
    print("删除功能")
    pass

print(__name__)
if __name__ == "__main__":
    msg = """
        1: 查询
        2：添加
        3：修改
        4：删除
        5: 退出
    """
    msg_dic = {
        "1":fetch,
        "2": add,
        "3": change,
        "4": delete,
        # "5":exit
    }
    while True:
        print(msg)
        choic = input("请输入你的选项：").strip()
        if not choic:continue
        if choic == "5":break
        data = input("请输入你的数据：").strip()
        msg_dic[choic](data)




