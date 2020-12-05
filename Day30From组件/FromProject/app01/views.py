from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.forms import UserForm
import json


# Create your views here.
def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'users.html', locals())


def add_user(request):
    """
    新增
    :param request:
    :return:
    """
    if request.method == 'POST':
        obj = UserForm(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'add_user.html', {'obj': obj})

    obj = UserForm()
    return render(request, 'add_user.html', locals())


def edit_user(request, nid):
    """
    编辑
    :param request:
    :param nid: user id
    :return:
    """
    if request.method == 'POST':
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'edit_user.html', {'obj': obj, 'nid': nid})
    data = models.UserInfo.objects.filter(id=nid).first()
    obj = UserForm({'username': data.username, 'email': data.email})
    return render(request, 'edit_user.html', {'obj': obj, 'nid': nid})


from django import forms as dforms
from django.forms import fields, widgets

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class AjaxForm(dforms.Form):
    username = fields.CharField()
    user_id = fields.IntegerField(
        widget=widgets.Select(choices=[(0, 'alex'), (1, '诸葛亮'), (2, '貂蝉'), (3, '程咬金')]),
    )

    # 对username二次校验,查看数据库中是否存在
    def clean_username(self):
        """
        自定义方法,clean_字段名
        必须返回值self.clean_data['username']
        如果出错,raise ValidationError('错误信息')
        :return:self.clean_data['username']
        """
        v = self.cleaned_data['username']
        if models.UserInfo.objects.filter(username=v).count():
            raise ValidationError('用户名已存在')
        return v

    def clean_user_id(self):
        return self.cleaned_data['user_id']

    # 联合唯一 多字段校验
    def clean(self):
        value_dict = self.cleaned_data
        v1 = value_dict.get('username')
        v2 = value_dict.get('user_id')
        print(v1, v2)
        if v1 == 'root' and v2 == 1:
            raise ValidationError('整体错误信息')
        return self.cleaned_data


def ajaxSub(request):
    if request.method == 'GET':
        obj = AjaxForm()
        return render(request, 'ajaxSub.html', {'obj': obj})
    else:

        ret = {'status': 1, 'msg': None}
        obj = AjaxForm(request.POST)
        print(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            ret['msg'] = '成功'
            return HttpResponse(json.dumps(ret))
        else:
            print(obj.errors.as_json())
            ret['status'] = 0
            ret['msg'] = obj.errors

            return HttpResponse(json.dumps(ret))


def xuliehua(request):
    """
    序列号
    :param request:
    :return:
    """
    # models.UserInfo.
    return render(request, 'xuliehua.html')


"""

def get_data(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'get_data.html',locals())
"""


def get_data(request):
    from django.core import serializers

    ret = {'status': True, 'data': None}
    try:
        # 序列化方式一 前端需要再次反序列化
        user_list = models.UserInfo.objects.all()
        ret['data'] = serializers.serialize('json', user_list)  # 对象序列化,变成字符串
    #     序列化方式二 前端不需要再次反序列化
        user_list = models.UserInfo.objects.values('id','username','email')
        ret['data'] = list(user_list)
    except Exception as e:
        ret['status'] = False

    result = json.dumps(ret)

    return HttpResponse(result)
