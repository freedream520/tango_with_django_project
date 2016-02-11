from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 

#从 django.db.models.Model 继承
#不同类型的 Field and validataors
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    #slugify 将 url 的空格变成 '-'，下面是将 save() 覆盖
    #使每次保存时都会 slugify URL 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    #Like __str__ 当 print 时打印出的字符串
    def __unicode__(self):
        return self.name 
        
class Page(models.Model):
    category = models.ForeignKey(Category)#表示的是 Category object 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title 
        
class UserProfile(models.Model):
    #将当前模型与 User 模型连接
    #因为其他应用可能也要使用 User，所以使用这个而不是继承自 User 
    user = models.OneToOneField(User)
    
    #自定义的 attributes      #允许不填写
    website = models.URLField(blank=True)
                                #与设置中的 MEDIA_ROOT join 组成储存图片文件夹
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username 

