from django import forms as dforms
from django.forms import fields

class UserForm(dforms.Form):
    username = fields.CharField(max_length=32)
    email = fields.EmailField(max_length=32)