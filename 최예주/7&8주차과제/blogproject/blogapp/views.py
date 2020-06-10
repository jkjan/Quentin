from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Portfolio
from .form import BlogPost
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page) 
    return render(request, 'home.html', {'blogs':blogs , 'posts':posts})

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

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect '})
    else :
      return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       return redirect('home')
    return render(request, 'login.html')


    
def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    #2. 빈 페이지를 띄워주는 기능  -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_data = timezone.now()
            post.body
            post.save()
            return redirect('home')
    else : 
        form = BlogPost()
        return render(request, 'new.html', {'form':form})