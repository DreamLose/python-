from django.shortcuts import render,redirect
from app import models
def get_students(request):
    std_list =models.Student.objects.all()

    return render(request,'get_student.html',locals())


def add_student(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender=request.POST.get('gender')
        cs_id = request.POST.get('cs')
        models.Student.objects.create(name=name,gender=gender,age=age,cs_id=cs_id)
        return redirect('/get_student.html')
    cs_list = models.Classes.objects.all()
    return render(request,'add_student.html',locals())


def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/get_student.html')

def edit_students(request):
    if request.method == "POST":
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs_id = request.POST.get('cs')
        print(request.POST)
        models.Student.objects.filter(id=nid).update(name=name,age=age,gender=gender,cs_id=cs_id)
        return redirect('/get_student.html')

    cs_list = models.Classes.objects.all()
    nid = request.GET.get('nid')
    std_info = models.Student.objects.filter(id=nid).first()
    return render(request,'edit_student.html',locals())