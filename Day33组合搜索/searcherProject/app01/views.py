from django.shortcuts import render,HttpResponse
from app01 import models
import json
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

# 瀑布流
def get_imgs(request):
    # nid = request.GET('nid')
    img_list = models.Img.objects.values('id','src','title')
    img_list = list(img_list)
    ret = {'status':True,'data':img_list}
    # return HttpResponse(json.dumps(ret))
    return JsonResponse(ret)   #只能返回字典 ,如果返回数组 JsonResponse(ret,safe=False)





"""
组合查询
"""
def searcher(request,*args,**kwargs):
    condition = {} #查询视频资源条件
    for key,val in kwargs.items():
        temp = int(val)
        kwargs[key] = temp

    print(kwargs)
    direction_id = kwargs['direction_id']
    classification_id = kwargs['classification_id']
    level_id = kwargs['level_id']
    direction_list = models.Direction.objects.all()
    if direction_id == 0:
        class_list = models.Classification.objects.all()
        if classification_id == 0:
            pass
        else:
            condition['classification_id'] = classification_id
    else:
        direction_obj = models.Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()
        vlist = direction_obj.classification.all().values_list('id')
        if not vlist:
            classification_id_list = []
        else:
            classification_id_list = list(zip(*vlist))[0]
        if classification_id == 0:
            condition['classification_id__in'] = classification_id_list
        else:
            if classification_id in classification_id_list:
                condition['classification_id'] = classification_id
            else:
                kwargs['classification_id'] = 0
                # 指定方向,分类不在其中
                condition['classification_id__in'] = classification_id_list
    if level_id == 0:
        pass
    else:
        condition['level_id'] = level_id

    level_list = models.Level.objects.all()
    video_list = models.Video.objects.filter(**condition)
    return render(request, 'searcher.html', locals())


