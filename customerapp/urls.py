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
from customerapp import views

urlpatterns = [
    # 최초 페이지
    path('', views.main_call, name="main_call"),

    # 로그인 페이지
    path('login', views.login_call, name="login_call"),

    # 로그아웃
    path('logout', views.logout),

    # 신청 페이지
    path('request', views.request_call, name="request_call"),

    # 신청
    path('client_request', views.clientRequest),

    # 신청 리스트 페이지
    path('request_list', views.request_list_call, name="request_list_call"),

    # 비밀번호 확인
    path('checkpassword', views.checkpassword, name="checkpassword"),

    # 신청 사항 페이지
    path('reading_request', views.reading_request_call, name="reading_request_call"),
]
