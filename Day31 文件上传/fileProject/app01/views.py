from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.forms import fields


# Create your views here.

class uploadFrom(forms.Form):
    user = fields.CharField()
    img = fields.FileField()


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        obj = uploadFrom(request.POST, request.FILES)
        if obj.is_valid():
            user = obj.cleaned_data['user']
            img = obj.cleaned_data['img']

            # user = request.POST.get('user')
            #  # img 是对象,(文件大小,名称,内容)
            #  img = request.FILES.get('img')
            print(img.name)
            print(img.size)
            f = open(img.name, 'wb')
            for line in img.chunks():
                f.write(line)
            f.close()

            return HttpResponse('ok')
