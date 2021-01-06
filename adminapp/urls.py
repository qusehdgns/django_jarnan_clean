"""clean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from adminapp import views

urlpatterns = [
    # 요청 리스트 페이지
    path('request_list', views.admin_request_list_call, name="admin_request_list_call"),
    
    # 요청 확인 페이지
    path('request_check', views.admin_request_call, name="admin_request_call"),

    # 댓글 삭제
    path('deletereply', views.deletereply),

    # 댓글 수정
    path('updatecomment', views.updatecomment),

    # 댓글 달기
    path('adminreply', views.adminreply),

    # 관리자 메모 수정
    path('updateadminmemo', views.updateadminmemo),
]
