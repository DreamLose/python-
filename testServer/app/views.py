from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    print(req.GET)
    # print(req.FIFES)
    return HttpResponse('注册成功')