from django.contrib import admin
from rango.models import Category, Page 

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    #输入类别的名称后自动 pre-populate slug field 
    prepopulated_fields = {'slug':('name',)}
    
# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

