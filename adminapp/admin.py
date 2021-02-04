from django.contrib import admin
from adminapp.models import User, Request, RequestItem, Construction, Comment, Review

# 출력할 ResourceAdmin 클래스를 만든다
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_pw')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'client_name', 'client_phone', 'request_address',
    'request_size', 'request_date', 'request_level','request_memo', 'admin_memo', 'read_password',
    'read_check', 'upload_date')

class RequestItemAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'item1', 'item2', 'item3', 'item4', 'item5',
    'item6', 'item7', 'item8', 'item9', 'item10', 'item11')

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'writer', 'reply_value', 'reply_date')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('r_num', 'writer', 'scope', 'review_value', 'review_date')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(RequestItem, RequestItemAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Review, ReviewAdmin)