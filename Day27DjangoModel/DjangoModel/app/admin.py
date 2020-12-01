from django.contrib import admin
from app import models
# Register your models here.



class AuthoAdmin(admin.ModelAdmin):
    list_display = ('id','name','age')

admin.site.register(models.Book)
admin.site.register(models.Publish)
admin.site.register(models.Author,AuthoAdmin)
