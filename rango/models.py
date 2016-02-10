from django.db import models
from django.template.defaultfilters import slugify

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

