"""Day29 URL Configuration

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
from django.urls import path
from app01 import views
from app02 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',views.students),
    path('add_student/',views.add_student),
    path('del_student/',views.del_student),
    path('edit_student/',views.edit_student),
    path('index/',views.index),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('form1/', v2.form1),

]
