from django.shortcuts import render,HttpResponse

def ajaxtest(request):
    return render(request,'ajax.html')

def ajax2(request):
    # list = request.GE
    print(request.GET)
    return HttpResponse('成功!')