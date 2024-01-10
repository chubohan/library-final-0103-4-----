"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as site
from myform import views as mf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',site.homepage,name='homepage'), #連到view的homepage
    path('post/<slug:slug>/',site.showpost,name="showpost"),
    path('function1/<slug:slug>/', site.function1, name='function1'),
    path('function2/<slug:slug>/', site.function2, name='function2'),
    path('function/<slug:slug>/', site.function, name='function'),
    path('search_books/',site.search_books, name='search_books'),
    path('borrow_return/',site.borrow,name='borrow_return'),
    path('register/',mf.register,name='register'),
    path('login/',mf.login,name='login'),
    path('logout/',mf.logout,name='logout'),
    path('username/',mf.userinfo,name='username'),
    path('msg/',mf.msg,name='msg'),
    path('return_book/',site.return_book,name='return_book'),
]
