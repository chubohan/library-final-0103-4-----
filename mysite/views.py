from django.shortcuts import render
from mysite.models import Post,Function,Function1,Function2,SearchKeyword,Borrow
from datetime import datetime
from django.shortcuts import redirect
from mysite.form import BorrowForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/msg/')
def homepage(request):
    selected_menu = request.GET.get('menu','home') #預設
    posts=Post.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        
    if selected_menu == "home":
        abc=Post.objects.all()
    elif selected_menu == "qa":
        abc=Function1.objects.all()
    elif selected_menu == "activity":
        abc=Function2.objects.all()
    elif selected_menu == "rule":
        abc=Function.objects.all()
    now=datetime.now()
    return render(request,'index.html',{'selected_menu': selected_menu, 'abc': abc,'username':username})

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, 'post.html', {'post': post})
    except Function1.DoesNotExist:
        return redirect("/") 
   
def function1(request, slug):#QA
    try:
        book = Function1.objects.get(slug2=slug)
        return render(request, 'qa.html', {'book': book})
    except Function1.DoesNotExist:
        return redirect("/") 
    
def function2(request, slug):#活動
    try:
        act = Function2.objects.get(slug3=slug)
        return render(request, 'activity.html', {'act': act})
    except Function1.DoesNotExist:
        return redirect("/") 
    
def function(request, slug):#規則
    try:
        ru = Function.objects.get(slug1=slug)
        return render(request, 'rule.html', {'ru': ru})
    except Function.DoesNotExist:
        return redirect("/") 
        
def search_books(request):
    if request.method == 'GET':
        search_query = request.GET.get('keyword', '')
        books = Post.objects.filter(title__icontains=search_query)
        return render(request, 'search.html', {'books': books})
    else:
        return render(request, 'search.html', {'books': []})
    
from datetime import datetime
@login_required(login_url='/msg/')
def borrow(request):
    posts = Borrow.objects.filter(enabled=True).order_by('-pub_time')[:30]
    abc=Post.objects.all()
    username = request.user.username
    if request.method == 'GET':
        form=BorrowForm()
        return render(request, 'myform.html', locals())
    elif request.method == 'POST':
        form=BorrowForm(request.POST)
        book_name = request.POST['book_name']
        borrow_date_str = request.POST['borrow_date']
        return_date_str = request.POST['return_date']

        # 转换日期字符串为日期对象
        borrow_date = datetime.strptime(borrow_date_str, '%Y-%m-%d').date()
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
        
        # 比较日期
        if return_date >= borrow_date:
            # 执行借书操作
            borrow_entry = Borrow(nickname=username, book_name=book_name, borrow_date=borrow_date_str, return_date=return_date_str)
            borrow_entry.save()
            message = '借書成功'
        else:
            message = '還書日期不能早於借書日期'
        return render(request, 'myform.html', locals())
    else:
        message = 'post/get 出現錯誤'
        return render(request, 'myform.html', locals())

   
#Borrow get不到值
@login_required(login_url='/msg/')

def return_book(request):
    posts = Borrow.objects.filter(enabled=True).order_by('-pub_time')[:30]
    abc = Borrow.objects.all()
    username = request.user.username
    now = datetime.now()
    user_borrowed_books = Borrow.objects.filter(user=request.user, enabled=True)
    
    if request.user.is_authenticated:
        current_user = request.user
        
    if request.method == 'GET':
        form = BorrowForm()
        if not user_borrowed_books:
            message = '無借書'
        
        return render(request, 'myform2.html', locals())
    if request.method == 'POST':
        current_user = request.user
        borrowed_book = Borrow.objects.get(user=current_user, enabled=True)
        book = borrowed_book.book_name
        form = BorrowForm(initial={'user_name': current_user.username, 'book_name': book})
        if form.is_valid():
            # 获取表单中的书名
            book_name = form.cleaned_data['book_name']
        
            # 在数据库中找到对应的借书记录
            issued_book = Borrow.objects.filter(book_name=book_name, nickname=username, enabled=True).first()
        
            if issued_book:
                # 进行还书操作
                issued_book.enabled = False
                issued_book.save()
                message = '還書成功'
            else:
                message = '找不到對應的借書記錄'
        else:
            print(request.POST)
            print(form.errors)
            message = '表單驗證失敗'

        return render(request, 'myform2.html', locals())




'''
function1=Function1.objects.all()
    return render(request,'qa.html',locals())

    try:
        book = Book1.objects.get(name=book_name)
        return render(request, 'book.html', {'book': book})
    except Book1.DoesNotExist:
        return redirect("/") 

'''
