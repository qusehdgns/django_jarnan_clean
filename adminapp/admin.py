from django.contrib import admin
from adminapp.models import User

# 출력할 ResourceAdmin 클래스를 만든다
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_pw')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)