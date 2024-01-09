from django.contrib import admin
from myform.models import Borrow
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','book_name', 'pub_time', 'enabled')
    
admin.site.register(Borrow, PostAdmin)
