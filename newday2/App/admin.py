from django.contrib import admin

# Register your models here.
from .models import User
from .models import MyBook

class UserAdmin(admin.ModelAdmin):
    list_display = ('u_name','u_age','u_score')
    list_filter = ('u_name','u_age','u_score')
    search_fields = ['u_name','u_age','u_score']
admin.site.register(User,UserAdmin)

#富文本注册
class MyBookAdmin(admin.ModelAdmin):
    list_display = ['m_name']
admin.site.register(MyBook,MyBookAdmin)