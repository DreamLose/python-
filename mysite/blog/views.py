from django.shortcuts import render,HttpResponse,redirect
import time,datetime
# Create your views here.
def show_time(request):
    t = time.ctime()
    name='诸葛亮'
    return render(request,'index.html',locals())
    # return render(request,'index.html',{'t':t,'name':name})



def article_year(request,year):

    return HttpResponse("year:%s month: %s"%year)


def year_month(request,year,month):
    return HttpResponse("year:%s month: %s"%(year,month))

def register(request):
    print(request.path) # 路径
    print(request.get_full_path()) # 带着数据的路径
    # if request.GET:
    #     print(request.GET)
    #     return HttpResponse('ok')
    if request.method == 'POST':
        print(request.POST)
        user = request.POST.get('user')
        if user=='yuan':
            return redirect('/ blog/login/')
            # return render(request,'login.html')
        return HttpResponse('ok')

    return render(request,'register.html')
    # return HttpResponse('ok')
def login(requset):
    # name = 'yuan'
    return render(requset,'login.html',locals())

class Animal():
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

def query(req):
    l = ['窜这个','诸葛亮','苍井空']
    d= {'name':'貂蝉','age':35,'sex':'女'}
    c = Animal('卢布',19)
    test = 'hello world!'
    test1 = 'h el lo w or ld !'
    t = datetime.datetime.now()
    e = []
    a = "<a href="">click</a>"
    dd = None
    return render(req,'query.html',locals())


def backend(request):
    return render(request,'base.html')

def student(request):
    student_list = ['诸葛亮','貂蝉','吕布','程咬金','张飞']
    return render(request,'student2.html',locals())
