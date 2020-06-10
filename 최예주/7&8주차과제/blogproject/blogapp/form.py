from django import forms
from .models import Blog

#model을 기반으로 한 입력공간 만들기 
"""
class BlogPost(forms.ModelForm):
    class Meta:
        #Blog모델을 기반으로 만들거임 
        model = Blog
        #어떤 항목을 만들건지
        field = ['title', 'body']
    """

#임의의 입력공간 만들기
class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','ones'),('2','two'),('3','three')])
