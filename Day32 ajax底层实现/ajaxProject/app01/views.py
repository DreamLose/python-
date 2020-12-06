from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def index(request):
    return render(request,'index.html')




def ajax1(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    return HttpResponse(json.dumps({'status':True,'msg':'ok'}))





def jsonp(resquest):
    return render(resquest,'jsonp.html')

def ajax3(request):
    return HttpResponse('本地服务器发送')