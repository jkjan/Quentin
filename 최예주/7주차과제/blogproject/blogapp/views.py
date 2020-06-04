from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Portfolio

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

# 단순히 new.html을 띄워주는 함수 
def new(request):
    return render(request, 'new.html')

#입력박은 내용을 데이처베이스에 넣어주는 함수 
def create(request):
    blog = Blog()   #객체 생성 
    blog.title = request.GET['title'] 
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()  # 작성한 시점 
    blog.save() # 
    return redirect('/blog/'+str(blog.id)) ##위에 있는거 다 처리한다음에 이 url로 이동하세염 

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})