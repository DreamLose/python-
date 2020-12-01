from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
    print(request.COOKIES)
    print(request.session)
    if request.method=="POST":
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(name,pwd)
        if name=='yuan' and pwd=='123':
            # ret = redirect('/index/')
            # ret.set_cookie('username',name)
            # 设置cookie 10s过期
            # ret.set_cookie('username', name,max_age=10)
            #
            # return ret
    # cookie && session
            request.session['is_login'] = True
            request.session['user'] = name
            return redirect('/index/')

    return render(request,'login.html')

def index(request):
    # print(request.COOKIES.get('isLogin'))
    # if request.COOKIES.get('username',None):
    #     name=request.COOKIES.get('username',None)
    #     return render(request, 'index.html', locals())
    if request.session.get('is_login',None):
        name=request.session.get('user',None)
        return render(request,'index.html',locals())
    return redirect('/login/')



from django.views import View

class CBV(View):
    # 重写父类的dispatch
    # cbv方式 get post 请求都 会走这个方法,
    def dispatch(self, request, *args, **kwargs):
        print('dispatch-------------')
        result =super(CBV,self).dispatch(request, *args, **kwargs)
        return result

    def get(self,request):
        return HttpResponse('GET')

    def post(self,request):
        ret = HttpResponse('POST')
        ret['h1'] = 'v1'
        ret.set_cookie('c1','c2')
        """
        头
            h1 = v1
            cookies:c1 = v1
        体
            POST
        """
        return HttpResponse('POST')

