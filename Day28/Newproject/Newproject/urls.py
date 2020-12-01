"""Newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,re_path
from app.views import classes
from app.views import student
from app.views import ajaxTest
urlpatterns = [
    path('admin/', admin.site.urls),
    # 班级管理
    re_path(r'classes.html$',classes.get_classes),
    re_path(r'add_class.html$',classes.add_class),
    re_path(r'del_class.html$',classes.del_class),
    re_path(r'edit_class.html$',classes.edit_class),
    # 学生管理
    re_path(r'student.html$', student.get_students),
    re_path(r'add_students.html$', student.add_student),
    re_path(r'del_students.html$',student.del_students),
    re_path(r'edit_students.html$',student.edit_students),
    # 教师管理

    re_path(r'set_teacher.html',classes.set_teacher),

    path('ajax1/',ajaxTest.ajaxtest),
    path('ajax2/',ajaxTest.ajax2),

]
