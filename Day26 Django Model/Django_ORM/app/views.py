from django.shortcuts import render,HttpResponse

from app.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
# 新增操作
def addbook(request):
    # 单表操作
    # 方式一
    # b=Book(name='python',price=99,author='alex',pub_date='2020-12-12',desc='简介')
    # b.save()
    # 方式二
    # Book.objects.create(name='计算机基础',price=99,author='诸葛亮',pub_date='2020-02-12',desc='简介')

    # 多表操作
    # 方式一
    # Book.objects.create(name='计算机基础',price=120,author='诸葛亮',pub_date='2012-3-29',desc='简介',publish_id=1)

    # 方式二:
    # 现获取关联表的对象
    # publish_obj = Publish.objects.filter(name='北京科技出版社')[0]
    # # 添加
    # Book.objects.create(name='linux运维', price=100, author='貂蝉', pub_date='2012-4-29', desc='简介', publish=publish_obj)

    # 一对多  object.publish --->一定是一个对象 正向查询 book-->查询出版社
    # object = Book.objects.get(name='linux运维')
    # print(object.publish.name)


    # 查询南方出版社的书籍 逆向查训 : 出版社-->查询出版的书籍
    # 方式一
    # pub_obj = Publish.objects.filter(id=3)[0]
    # ret = Book.objects.filter(publish=pub_obj).values('name','price')
    # print(ret)
    # 方式二
    # pub_obj = Publish.objects.filter(id=3)[0]
    # print(pub_obj.book_set.all().values('name','price'))
    # 方式三 (filter values 双下划线__)
    ret = Book.objects.filter(publish__name='南方出版社').values('name','price')
    print(ret)

    #python 出版社的信息
    ret = Publish.objects.filter(book__name='linux运维').values('name')
    print(ret)
    ret = Book.objects.filter(name='linux运维').values('publish__name')
    print(ret)
    # 查询北京出版社出版的书
    ret = Publish.objects.filter(city='北京').values('book__name','name')
    print(ret)
    ret = Book.objects.filter(publish__city='北京').values('name')
    print(ret)

    return HttpResponse('添加成功!')
# 更新操作
def updata(request):
    # 方式一
    Book.objects.filter(author='alex').update(price=120)
    # 方式二
    # b = Book.objects.get(author='alex')
    # # print(b,type(b))   --><QuerySet [<Book: Book object (1)>]> <class 'django.db.models.query.QuerySet'>
    # b.name='python基础'
    # b.save()
    return HttpResponse('更新成功!')
# 删除操作
def deletebook(req):
    Book.objects.filter(author='alex').delete()
    return HttpResponse('删除成功!')
# 查询操作

def selectBook(req):
    """
    # 查找全部
    # book_list = Book.objects.all()
    # print(book_list[0])
    book_list = Book.objects.all()[::2]
    # 拿到一个集合
    # book_list = Book.objects.filter(id=2)
    # 第一个/最后一个
    # book_list = Book.objects.first()
    # book_list = Book.objects.last()
    # 拿到的是一个对象,只能取出一条记录的时候才不会报错,两条以上或者0条都会报错
    # book_list = Book.objects.get(name='alex')
    # 只拿到name的值
    ret = Book.objects.filter(author='貂蝉').values('name','price')
    print(ret)  # [{'name': 'python基础', 'price': 90.0}]
    ret = Book.objects.filter(author='貂蝉').values_list('name', 'price')
    print(ret)   # [('python基础', 90.0)]>
    # 遍历作者不是貂蝉的数据
    # book_list = Book.objects.exclude(author='貂蝉').values('name','price')
    # distinct()
    book_list = Book.objects.all().values('name').distinct()
    # 万能的__ 下划线 模糊查询
    book_list = Book.objects.filter(price__gt=50).values('name','price')
    #  不区分大小写  contains 大写
    book_list = Book.objects.filter(name__icontains='p ').values('name', 'price')
    """
    book_list = []
    return render(req,'index.html',{'book_list':book_list})

# 多对多
def manyTomany(req):
    # 通过对象绑定关系
    # book_obj = Book.objects.get(id=3)
    # print(book_obj.author.all())
    # author_obj = Author.objects.get(id=2)
    # print(author_obj.book_set.all())
    # 添加
    # book_obj = Book.objects.get(id=5)
    # # author_obj = Author.objects.get(id=2)
    # # book_obj.author.add(author_obj)
    # author_obj = Author.objects.all()
    # # book_obj.author.add(*author_obj)  # 一个数组,前面要加*

    #删除全部
    # book_obj.author.remove(*author_obj)

    # book_obj.author.remove(2)


    # 创建第三张表

    # Book_Author.objects.create(book_id=2,author_id=3)
    # obj=Book.objects.get(id=2)
    # print(obj.book_author_set.all()[0].author)
    #
    # alex 出过的书籍名称及价格
    ret = Book.objects.filter(book_author__author__name='alex').values('name','price')
    print(ret)
    return HttpResponse('添加成功!')