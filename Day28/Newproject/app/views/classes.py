from django.shortcuts import render ,redirect,HttpResponse
from app import models
def get_classes(request):
    cls_list = models.Classes.objects.all()

    return render(request,'get_classes.html',locals())

def add_class(request):
    if request.method=='POST':
        title = request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect('/classes.html')
    else:
        return render(request,'add_class.html')

def del_class(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')

def edit_class(request):
    if request.method=='POST':
        nid = request.POST.get('nid')
        title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes.html')
    else:
        nid = request.GET.get('nid')
        n_class = models.Classes.objects.get(id=nid)
        return render(request,'edit_class.html',locals())

def set_teacher(request):
    if request.method=='POST':
        # print(request.POST.getlist('teacher_ids'))
        teacher_ids = request.POST.getlist('teacher_ids')
        nid = request.POST.get('nid')
        # 更新班级老师信息
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_obj.teacher.set(teacher_ids)
        return redirect('/get_classes.html')
    else:
        nid = request.GET.get('nid')
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_teacher_list = cls_obj.teacher.all()
        all_teachers = models.Teachers.objects.all()
        return render(request,'set_teacher.html',locals())
