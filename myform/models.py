from django.db import models

# Create your models here.


class Borrow(models.Model):
    
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    book_name = models.CharField(max_length=10)
    return_date=models.TextField(max_length=20)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return self.message