from django.shortcuts import render,HttpResponse
from app.models import *
from django.db.models import *
# Create your views here.

def handleBook(request):
    # 聚合
    # ret = Book.objects.all().aggregate(Avg('price'))
    # ret = Book.objects.all().aggregate(Sum('price'))
    ret = Book.objects.filter(authors__name='alex').aggregate(alex_money=Sum('price'))

    # 分组
    ret = Book.objects.values('authors__name','price').annotate(Sum('price'))

    #
    # select app_book_

    return HttpResponse('操作成功!')