from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug =models.CharField(max_length=200)
    body =models.TextField()
    author=models.CharField(max_length=200)
    publishing=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-pub_date',)
    def __str__(self):
        return self.title

class Function(models.Model):
    rule=models.CharField(max_length=200)
    slug1 = models.CharField(max_length=200, default='your_default_value_here') #預設值
    def __str__(self):
        return self.rule

class Function1(models.Model):
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    slug2 = models.CharField(max_length=200, default='your_default_value_here')
    def __str__(self):
        return self.question

class Function2(models.Model):
    activity=models.CharField(max_length=200)
    activitytime=models.CharField(max_length=200)
    activitypeople=models.CharField(max_length=200)
    activityplace=models.CharField(max_length=200)
    activitycontant=models.TextField(max_length=200)
    activitynotice=models.TextField(max_length=200)
    slug3 = models.CharField(max_length=200, default='your_default_value_here')
    def __str__(self):
        return self.activity


class SearchKeyword(models.Model):
    keyword = models.TextField()

    def __str__(self):
        return self.keyword

from django.contrib.auth.models import User


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    nickname = models.CharField(max_length=40)
    borrow_date = models.TextField(null=False)
    book_name = models.CharField(max_length=40)
    return_date = models.TextField(max_length=40)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
    
    