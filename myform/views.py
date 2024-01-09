from django.shortcuts import render,redirect

from myform.form import UserRegisterForm,LoginForm

# Create your views here.
'''
from myform.models import Post
def index(request):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    if request.method == 'GET':
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        user_id = request.POST['user_id']
        book_name = request.POST['book_name']
        borrow_date = request.POST['borrow_date']
        return_date = request.POST['return_date']
        post = Post(nickname=user_id, book_name=book_name, message=borrow_date,return_date=return_date)
        post.save()
        message = f'123'
        return render(request, 'myform.html', locals())
    else:
        message = 'post/get 出現錯誤'
        return render(request, 'myform.html', locals())
'''    

from django.contrib.auth.models import User

def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功！'
            else:
                message = f'兩次密碼不一致！'    
        return render(request, 'register.html', locals())
    else:
        message = "ERROR"
        return render(request, 'register.html', locals())
    
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None: #如果帳號有註冊
                if user.is_active:
                    auth.login(request, user)
                    message = '成功登入 請點選想瀏覽的頁面'
                    username = request.user.username
                    if user.is_staff:
                        message = '你是管理員'
                       
                    return render(request, 'login.html', locals())
                else:
                    message = '帳號尚未啟用'
            else:
                message = '登入失敗'

        return render(request, 'login.html', locals())
    else:
        message = "ERROR"
        return render(request, 'login.html', locals())

@login_required(login_url='/msg/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        email=request.user.email
        
    return render(request, 'userinfo.html', locals())

def msg(request):
    message='請先登入'
    if request.user.is_authenticated:
        message='登出成功'   
    return render(request, 'msg.html', locals())


@login_required(login_url='/msg/')
def logout(request):
    auth.logout(request)
    message='我登出囉'
    return render(request, 'logout.html', locals())


'''
def staff(request):
    condition=True
    return render(request,'base.html',locals())
'''