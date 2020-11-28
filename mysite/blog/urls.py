from django.contrib import admin
from django.urls import path,re_path,include
from blog import views

urlpatterns = [
    # path('articles/\d{4}', views.article_year),
    # 无命名分组
    re_path(r'articles/(\d{4})$', views.article_year),
    # 命名分组
    re_path(r'/(?P<year>\d{4})/(?P<month>\d{2})', views.year_month),
    path('register/', views.register, name='reg'),
    path('login/',views.login,name='login'),
    path('query/', views.query),
    path('backend/',views.backend,name='backend'),
    path('student/',views.student,name='student'),

#     分发
]
