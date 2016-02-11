from django import forms 
#为这两个 Model 制定表格
from rango.models import Page, Category 

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, 
        help_text="Please enter the title of the page.")
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
        help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, 
        help_text='Please enter the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Page 
        #fields 表示包含进来的 exclude 表示不需要包含进来的，可能会造成错误
        #Category object 
        exclude = ('category',)