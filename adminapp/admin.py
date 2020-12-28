from django.contrib import admin
from adminapp.models import User, Request, RequestItems, Construction, Comment

# 출력할 ResourceAdmin 클래스를 만든다
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_pw')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'client_name', 'client_phone', 'request_address',
    'request_date', 'request_size', 'request_memo', 'admin_memo', 'read_password',
    'read_check', 'upload_date')

class RequestItemsAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'item1', 'item2', 'item3', 'item4', 'item5',
    'item6', 'item7', 'item8', 'item9', 'item10', 'item11', 'item12')

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'item1', 'item2', 'item3', 'item4', 'item5')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'writer', 'reply_value', 'reply_date')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(RequestItems, RequestItemsAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Comment, CommentAdmin)