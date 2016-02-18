from django.test import TestCase, LiveServerTestCase
from rango.models import Category, Page 
from django.core.urlresolvers import reverse 
import datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

def add_category(name, views=1, likes=1):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views 
    category.likes = likes
    category.save()
    return category 
    
def add_page(category, title, first_visit, last_visit, url="http//:www.baidu.com", views=1):
    page = Page.objects.get_or_create(category=category, title=title, first_visit=first_visit, last_visit=last_visit, url=url, views=views)[0]
    # page.category = category 
    # page.title = title 
    # page.url = url 
    # page.views = views 
    # page.first_visit = first_visit
    # page.last_visit = last_visit 
    
    return page 

class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        views 应该 >= 0 
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

class PageMethodTests(TestCase):
    def test_visit_not_in_future(self):
        """
        first_visit and last_visit should <= datetime.datetime..now()
        #为了测试间独立，每个测试完后不要清空数据？ wait 
        """
        #初始化
        category = add_category('testdfs')
        now = datetime.datetime.now(datetime.timezone.utc)
        first_visit = now - datetime.timedelta(hours=2)
        #设置为未来时间
        last_visit = now + datetime.timedelta(hours=2)
        page1 = add_page(category=category, title="test", first_visit=first_visit, last_visit=last_visit)
        page1.save()
                        
        self.assertFalse(page1.last_visit > now)
    
    def test_last_visit_equal_or_after_first_visit(self):
        """
        last_visit 时间应该等于或者大于 first_visit
        """
        #初始化
        category = add_category('test_last_visit_equal_or_after_first_visit')
        now = datetime.datetime.now(datetime.timezone.utc)
        #设置 last_visit 小于 first_visit 应该返回 last_visit 大于或等于 first_visit
        first_visit = now        
        last_visit = now - datetime.timedelta(hours=2)
        page = add_page(category=category, title="test", first_visit=first_visit, last_visit=last_visit)
        page.save()
                        
        self.assertEqual((page.last_visit > page.first_visit or page.last_visit == page.first_visit), True)
        
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
        
class AccountTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()
        
    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    """
    测试注册功能    
    """
    def test_register(self):
        selenium = self.selenium 
        #打开注册链接 
        selenium.get("http://127.0.0.1:8000/accounts/register/")
        
        #通过 name="xxx" 找到表单元素
        username = selenium.find_element_by_name('username')
        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')
        register = selenium.find_element_by_name('register')
        
        #填充数据到表单
        username.send_keys('test')
        email.send_keys('test@qq.com')
        password1.send_keys('test')
        password2.send_keys('test')
        
        #提交数据到表单
        register.send_keys('Keys.RETURN')
        
        #检查结果
        self.assertContains(selenium.page_source, "Hello test!")
        