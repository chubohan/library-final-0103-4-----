from django.contrib import admin
from mysite.models import Post,Function,Function1,Function2,SearchKeyword
admin.site.register(SearchKeyword)
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','body','author','publishing','pub_date') #管理欄位
admin.site.register(Post, PostAdmin)


class FunctionAdmin(admin.ModelAdmin):
    list_display=('rule','slug1') #管理欄位

admin.site.register(Function, FunctionAdmin)


class Function1Admin(admin.ModelAdmin):
    list_display=('question','answer','slug2') #管理欄位

admin.site.register(Function1, Function1Admin)

class Function2Admin(admin.ModelAdmin):
    list_display=('activity','activitytime','activitypeople','activityplace','activitycontant','activitynotice','slug3') #管理欄位

admin.site.register(Function2, Function2Admin)

