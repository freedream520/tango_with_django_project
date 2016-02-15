from django import template
from rango.models import Category 

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list():
    # key 表示传递到 cats.html 的变量名 
    # 通过应用模板中的 {% get_category_list category %} 传递
    return {"cats": Category.objects.all(), 'act_cat': cat}