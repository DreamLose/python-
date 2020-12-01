from django.shortcuts import render ,redirect
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