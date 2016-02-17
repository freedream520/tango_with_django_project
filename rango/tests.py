from django.test import TestCase
from rango.models import Category, Page 
from django.core.urlresolvers import reverse 
from datetime import datetime 

def add_category(name, views=1, likes=1):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views 
    category.likes = likes
    category.save()
    return category 
    
def add_page(category, title, url="http:www.baidu.com", views=1, first_visit, last_visit):
    page = Page.objects.get_or_create(title=title)[0]
    page.category = category 
    page.title = title 
    page.url = url 
    page.views = views 
    page.first_visit = first_visit
    page.last_visit = last_visit 
    
    return page 

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        views 应该 >= 0 
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)
        
class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        #因为现在是在测试数据库中，分类一片空白
        根据代码，不存在的分类，应该显示 "There are no categories present"
        """        
        # reverse 查询到 'index' 视图函数对应的网址
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present")
        #A queryset 查询集等于后面 list
        self.assertQuerysetEqual(response.context['categories'], [])
        
    def test_index_view_with_categories(self):
        """
        如果存在分类，响应中包含分类的名称，分类个数匹配
        """        
        add_category('test')
        add_category('temp1')
        add_category('temp2')
        add_category('temp3')
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        #响应中包含分类的名称
        self.assertContains(response, "test")
        
        num_categories = len(response.context['categories'])
        self.assertEqual(num_categories, 4)