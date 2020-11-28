from django.shortcuts import render,HttpResponse

from app.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
# 新增操作
def addbook(request):
    # 方式一
    # b=Book(name='python',price=99,author='alex',pub_date='2020-12-12',desc='简介')
    # b.save()
    # 方式二
    Book.objects.create(name='计算机基础',price=99,author='诸葛亮',pub_date='2020-02-12',desc='简介')
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
    return render(req,'index.html',{'book_list':book_list})