from django.shortcuts import render, HttpResponse
from app01 import models
import json


# Create your views here.

def students(request):
    stu_list = models.Students.objects.all()
    cls_list = models.Classes.objects.all()

    return render(request, 'students.html', locals())


def add_student(request):
    # print(request.POST)
    response = {'status': True, 'msg': '添加成功'}
    username = request.POST.get('username')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    cs_id = request.POST.get('classes')
    try:
        obj = models.Students.objects.create(username=username, age=age, gender=gender, cs_id=cs_id)
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['msg'] = '用户输入错误'
        response['data'] = None
    return HttpResponse(json.dumps(response))


def del_student(request):
    nid = request.POST.get('nid')
    response = {'status': True, 'msg': '删除成功'}
    try:
        models.Students.objects.filter(id=nid).delete()
    except Exception as e:
        response['status'] = False
        response['msg'] = '删除失败'
    return HttpResponse(json.dumps(response))
def edit_student(request):

    response = {'code':1000,'msg':None}
    try:
        nid = request.POST.get('nid')
        gender = request.POST.get('gender')
        user = request.POST.get('user')
        cls_id = request.POST.get('cls_id')
        age = request.POST.get('age')
        models.Students.objects.filter(id=nid).update(username=user,age=age,gender=gender,cs_id=cls_id)
    except Exception as e:
        response['code'] = 1001
        response['msg'] = str(e)
    return HttpResponse(json.dumps(response))


#分页组件

USER_LIST = []
for i in range(1,666):
    temp={'name':'root'+str(i),'age':i}
    USER_LIST.append(temp)
def index(request):
    per_count = 10
    current_page=request.GET.get('p')
    current_page = int(current_page)

    start = (current_page -1) * per_count
    end = current_page * per_count
    data = USER_LIST[start:end]

    prev_page= current_page-1
    next_page = current_page+1
    return render(request,'index.html',{'users':data,'prev_page':prev_page,'next_page':next_page})

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# 扩展内置分页
class CustomPaginator(Paginator):
    def __init__(self,current_page,per_pager_num,*args,**kwargs):
        # 当前页
        self.current_page = int(current_page)
        # 最多显示的页码数量
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)
    # 定义默认显示的页码范围
    def pager_num_range(self):
        # 总页数
        # self.num_pages
        if self.num_pages < self.per_pager_num:
            return range(1,self.num_pages+1)
#         总页数特别多
        part = int(self.per_pager_num/2)
        if self.current_page <= part:
            return range(1,self.per_pager_num+1)
        # 如果当前页 加上 5 大于最多页
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages-self.per_pager_num+1,self.num_pages+1)
        return range(self.current_page-part,self.current_page+part+1)

# 内置分页组件
def index1(request):
    current_page = request.GET.get('p')

    # 全部数据 :USER_LIST   ->得出一共多少数据
    # 10 每页显示的条数

    # paginiator = Paginator(USER_LIST,10)
    paginiator = CustomPaginator(current_page,11,USER_LIST, 10)
    try:
        posts = paginiator.page(current_page)
    except PageNotAnInteger:
        posts = paginiator.page(1)
    except EmptyPage:
        posts = paginiator.page(paginiator.num_pages)
    return render(request,'index1.html',{'post':posts})

def index2(request):
    from app01.pager import Pagination
    current_page = request.GET.get('p')
    page_obj = Pagination(666,current_page,10)

    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request,'index2.html',{'data':data_list,'page_obj':page_obj})