from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django import forms
from django.forms import fields

class fqForm(forms.Form):
    user = fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '太长了',
            'min_length': '太短了',
        }
    )
    pwd = fields.CharField(min_length=32,required=True,
                           error_messages={
                               'required': '密码不能为空',
                               'min_length': '太长了',
                           })
    age = fields.IntegerField(required=True,
                              error_messages={
                                  'required': '年龄不能为空',
                                  'invalid': '格式错误',
                              }
                              )
    email = fields.EmailField(required=True,
                              error_messages={
                                  'required': '年龄不能为空',
                                  'invalid': '格式错误',
                              })



def form1(request):
    if request.method =='POST':
        obj = fqForm(request.POST)
        #  验证成功
        if obj.is_valid():
            # 用户提交的数据
            print(obj.cleaned_data)
            return redirect('http://www.baidu.com')
        else:
            print(obj.errors)
            return render(request,'form1.html',{'obj':obj})

    # 生成html代码
    obj = fqForm()

    return render(request,'form1.html',{'obj':obj})