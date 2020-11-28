from django import template
from django.utils.safestring import mark_safe
register = template.Library()  # register 名字是固定的,不可改变

# 自定义filter
@register.filter
def filter_multi(x,y):
    """最多传一个参数,x是默认的
    想传多个值,传一个列表就可以
    """
    return x*y


# 自定义标签,可以传多个值
@register.simple_tag
def simple_tag_multi(x,y):
    return x*y
