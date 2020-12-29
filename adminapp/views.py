# 웹 url 호출 시 html 및 템플릿 변수 전송
from django.shortcuts import render
# 웹 url 호출 시 다른 url로 이동
from django.shortcuts import redirect
# 웹에 문자열 리턴
from django.http import HttpResponse
# Json 형식의 데이터 리턴
from django.http import JsonResponse

# Json 형식 사용
import json

# 데이터베이스
from adminapp.models import User, Request, RequestItem, Construction, Comment

def admin_request_list_call(request):

    if request.session.has_key('name') == False:
        # 로그인 기록이 없을 경우
        return redirect('login_call')
    
    else:
        if request.session.has_key('id') == False:
            return redirect('request_list_call')
    
    if User.objects.filter(user_id = request.session['id']).exists() == False :
        # 관리자 인증 실패
        return redirect('request_list_call')
    
    return render(request, 'Admin_Request_List.html')