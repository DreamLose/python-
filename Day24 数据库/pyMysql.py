import pymysql
conn = pymysql.connect(host='192.168.0.103',port=3306,user='root',passwd='123',db='pyMysql')
# 默认返回的元组,添加括号内容返回的会是键值对
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql = 'create table test(id int,name varchar(20))'
# cursor.execute(sql)

# ret = cursor.execute("insert into test values (1,'诸葛亮'),(1,'貂蝉')")
# print(ret)

ret = cursor.execute("select * from test")
print(ret)

one = cursor.fetchone()
one = cursor.fetchone()
# 移动光标
# 相对位置
# cursor.scroll(-1,mode='relative')
# 绝对位置
cursor.scroll(1,mode='absolute')
all = cursor.fetchall()
print(all)

conn.commit()
cursor.close()
conn.close()