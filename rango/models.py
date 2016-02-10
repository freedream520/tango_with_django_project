from django.db import models

#从 django.db.models.Model 继承
#不同类型的 Field and validataors
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #Like __str__ 当 print 时打印出的字符串
    def __unicode__(self):
        return self.name 
        
class Page(models.Model):
    category = models.ForeinKey(Category)#不是Category.name？
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title 

