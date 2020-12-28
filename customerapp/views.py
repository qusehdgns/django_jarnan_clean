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
from adminapp.models import User, Request, RequestItems, Construction, Comment

clean = ['입주 청소','이사 청소','인테리어 후 청소','사무실 청소', '식당 청소', '준공 청소' ,'학교 청소', '관공서 청소','외벽 청소','거주 청소','계단 청소', '특수 청소']
construct = ['마루코팅','타일코팅','나노코팅','주방상판','대리석연마']

# Main 페이지 호출
def main_call(request):
    
    return render(request, 'Main.html')

# 로그인 페이지 호출
def login_call(request):
    print("실행");

    # Post 형식 데이터가 들어오는지 확인
    if request.method == "POST":
        # Post 형식 데이터를 data 변수에 저장
        data = request.POST

        print(data['clientPhone'])

        if request.session.has_key('name'):
            # 세션에 존재하는 name 삭제
            request.session.pop('name')
            
        if request.session.has_key('phone'):
            # 세션에 존재하는 name 삭제
            request.session.pop('phone')

        # name 세션에 아이디 저장
        request.session['name'] = data['clientName']

        # 관리자 아이디 확인
        if User.objects.filter(user_id = data['clientName'], user_pw = data['clientPhone']).exists() == True :
            # 관리자 인증 성공
            # name 세션에 아이디 저장
            request.session['id'] = data['clientName']

            return redirect('admin_request_list_call')
        
        else :
            # 관리자가 아닐 경우
            # name 세션에 아이디 저장
            request.session['phone'] = data['clientPhone']

            return redirect('request_list_call')

    return render(request, 'Login.html')

# 신청 페이지 호출
def request_call(request):
    # 로그인 안할 경우 기본값
    name = ""
    phone = ""

    # 로그인 후 접속일 경우
    if request.session.has_key('name'):
        name = request.session['name']
    # 로그인 후 접속일 경우
    if request.session.has_key('phone'):
        name = request.session['phone']

    return render(request, 'Request.html', { "name" : name, "phone" : phone, "clean" : clean, "construct" : construct })

# 신청 리스트 페이지
def request_list_call(request):

    # 로그인 후 접속일 경우
    if request.session.has_key('name') and request.session.has_key('phone'):
        return render(request, 'Request_List.html')

    return redirect('login_call')