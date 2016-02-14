from django import forms 
#为这两个 Model 制定表格
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, 
        help_text="Please enter the title of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
                                       #save 中会自动赋值给这个field
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    #提供额外信息给这个 form 
    class Meta:
        #我们想把这个 form 提供给哪个 model 
        model = Category
        #想从 model 中包含哪个 field 到这个 form 中，可以是多个
        fields = ('name',)
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, 
        help_text="Please enter the title of the page")
    url = forms.URLField(max_length=200, 
        help_text='Please enter the URL of the page')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Page 
        #fields 表示包含进来的 exclude 表示不需要包含进来的，可能会造成错误
        #Category object 
        exclude = ('category',)
    
    #因为输入的URL格式可能不正确，我们通过覆盖 clean()
    #函数来格式化 URL。在这个函数中加上检查的部分
    #因为 clean() 函数在储存表单数据前运行
    #扩展开来，form 表单中数据检查、处理也可以在这进行
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        #url 不为空并且不是以 'http://' 开头
        if url and not url.startswith('http://'):
            url = 'http://' + url 
            cleaned_data['url'] = url 
        
        return cleaned_data
        
class UserForm(forms.ModelForm):
    #使密码输入时不可见，model 中密码是可见的
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ('website', 'picture')