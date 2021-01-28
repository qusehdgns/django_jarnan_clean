# 웹 url 호출 시 html 및 템플릿 변수 전송
from django.shortcuts import render
# 웹 url 호출 시 다른 url로 이동
from django.shortcuts import redirect
# 웹에 문자열 리턴
from django.http import HttpResponse
# Json 형식의 데이터 리턴
from django.http import JsonResponse
# Post 통신 시 필요한 암호화를 우회
from django.views.decorators.csrf import csrf_exempt

# Json 형식 사용
import json
# 날짜 형식
from datetime import datetime as dt

# 데이터베이스
from adminapp.models import User, Request, RequestItem, Construction, Comment, Review

# 문자 api
from adminapp.sms_api import send_sms

clean = ['입주 청소', '이사 청소', '인테리어 후 청소', '사무실 청소', '식당 청소',
         '준공 청소', '학교 청소', '상가 청소', '외벽 청소', '거주 청소', '계단 청소', '특수 청소']
construct = ['마루코팅', '타일코팅', '나노코팅', '줄눈시공', '주방상판', '대리석연마']


# Main 페이지 호출
def main_call(request):

    reviewData = Review.objects.filter(scope=5).order_by('-review_date').values()[:5]

    reviews = []

    for data in reviewData:
        temp = ""
        for i in range(1,len(data['writer'])):
            temp += "*"
        
        temp = data['writer'][0] + temp
        
        dictval = { "writer" : temp, "review_value" : data['review_value'], "review_date" : data['review_date'], "scope" : data['scope'] }
        
        reviews.append(dictval)

    return render(request, 'Main.html', { "clean" : clean, "construct" : construct, "reviews" : reviews })

# 로그인 페이지 호출


def login_call(request):

    if request.session.has_key('phone'):
        # 세션에 존재하는 phone 삭제
        request.session.pop('phone')

    if request.session.has_key('name'):
        # 세션에 존재하는 name 삭제
        request.session.pop('name')

    if request.session.has_key('id'):
        # 세션에 존재하는 id 삭제
        request.session.pop('id')

    # Post 형식 데이터가 들어오는지 확인
    if request.method == "POST":
        # Post 형식 데이터를 data 변수에 저장
        data = request.POST

        # name 세션에 저장
        request.session['name'] = data['clientName']

        # 관리자 아이디 확인
        if User.objects.filter(user_id=data['clientName'], user_pw=data['clientPhone']).exists() == True:
            # 관리자 인증 성공
            # id 세션에 저장
            request.session['id'] = data['clientName']

            return redirect('admin_request_list_call')

        else:
            # 관리자가 아닐 경우
            # phone 세션에 저장
            request.session['phone'] = data['clientPhone']

            return redirect('request_list_call')

    return render(request, 'Login.html')

# 로그아웃


def logout(request):
    if request.session.has_key('phone'):
        # 세션에 존재하는 phone 삭제
        request.session.pop('phone')

    if request.session.has_key('name'):
        # 세션에 존재하는 name 삭제
        request.session.pop('name')

    if request.session.has_key('id'):
        # 세션에 존재하는 id 삭제
        request.session.pop('id')

    return HttpResponse()

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
        phone = request.session['phone']

    return render(request, 'Request.html', {"name": name, "phone": phone, "clean": clean, "construct": construct})


# 신청
@csrf_exempt
def clientRequest(request):
    # Post 형식 데이터 저장
    data = request.POST

    # name 세션에 아이디 저장
    request.session['name'] = data['clientName']

    # phone 세션에 저장
    request.session['phone'] = data['clientPhone']

    if data['requestLevel'] == "true":
        requestLevel = True
    else:
        requestLevel = False

    client = Request.objects.create(client_name=data['clientName'], client_phone=data['clientPhone'],
                                    request_address=data['requestAddress'], request_size=data['requestSize'],
                                    request_date=data['requestDate'], request_level=requestLevel,
                                    request_memo=data['requestMemo'], read_password=data['readPassword'])

    # 문자 발송
    send_sms(data)

    Itembool = [False for i in range(len(clean))]

    if data['requestClean'] != "":
        for temp in data['requestClean'].split(','):
            Itembool[clean.index(temp)] = True

    RequestItem.objects.create(r_num=client, item1=Itembool[0], item2=Itembool[1],
                               item3=Itembool[2], item4=Itembool[3], item5=Itembool[4],
                               item6=Itembool[5], item7=Itembool[6], item8=Itembool[7],
                               item9=Itembool[8], item10=Itembool[9], item11=Itembool[10],
                               item12=Itembool[11])

    Cunstructbool = [False for i in range(len(construct))]

    if data['requestConstruct'] != "":
        for temp in data['requestConstruct'].split(','):
            Cunstructbool[construct.index(temp)] = True

    Construction.objects.create(r_num=client, item1=Cunstructbool[0], item2=Cunstructbool[1],
                                item3=Cunstructbool[2], item4=Cunstructbool[3], item5=Cunstructbool[4],
                                item6=Cunstructbool[5])

    return HttpResponse(data['clientName'] + " 님 예약이 완료되었습니다.")


# 신청 리스트 페이지
def request_list_call(request):
    # 로그인 후 접속이 아닐 경우
    if request.session.has_key('name') == False or request.session.has_key('phone') == False:
        return redirect('login_call')

    # 세션 저장값 호출
    name = request.session['name']
    phone = request.session['phone']

    requestList = []

    for temp in Request.objects.filter(client_name=name, client_phone=phone).order_by('-upload_date').values():
        if temp['request_date'] < dt.now().date():
            if Review.objects.filter(r_num=temp['r_num']).exists() == False:
                temp['review'] = True

        requestList.append(temp)
    
    if requestList:
        requestList = enumerate(requestList, start=1)

    return render(request, 'Request_List.html',
                  {"name": name, 'requestList': requestList })


# 비밀번호 확인
@csrf_exempt
def checkpassword(request):
    # Post 형식 데이터 저장
    data = request.POST

    if Request.objects.filter(r_num=data['r_num'], read_password=data['readPassword']).exists() == True:
        return HttpResponse("success")

    return HttpResponse("fail")


# 신청 사항 페이지
def reading_request_call(request):
    # Post 형식 통신인지 확인
    if request.method == "POST":

        clientRequest = Request.objects.get(
            pk=request.GET['r_num'], read_password=request.POST['readPassword'])

        items = RequestItem.objects.filter(r_num=clientRequest).values()

        cleanItems = []

        for data in items:
            for index, value in enumerate(clean, start=1):
                if data['item' + str(index)]:
                    temp = { "clean" : value }
                    cleanItems.append(temp)
    
        if cleanItems:
            cleanItems = enumerate(cleanItems)

        constructs = Construction.objects.filter(r_num=clientRequest).values()

        constructions = []

        for data in constructs:
            for index, value in enumerate(construct, start=1):
                if data['item' + str(index)]:
                    temp = { "construct": value }
                    constructions.append(temp)
    
        if constructions:
            constructions = enumerate(constructions)
        
        comments = Comment.objects.filter(r_num=clientRequest).order_by("reply_date").values()

        replys = []

        for data in comments:
            temp = { 'id' : data['id'], 'writer' : data['writer'], 'reply_value' : data['reply_value'] }
            replys.append(temp)
        
        reviews = None
        
        if Review.objects.filter(r_num=clientRequest).exists() == True:
            reviews = Review.objects.get(r_num=clientRequest)

        return render(request, "Reading_Request.html",
                      {"request": clientRequest, "items": cleanItems,
                      "constructs": constructions, 'comments' : replys,
                      "review" : reviews })

    return redirect("request_list_call")


# 클라이언트 댓글
@csrf_exempt
def clientreply(request):
    # Post 형식 데이터 수신
    data = request.POST

    clientRequest = Request.objects.get(pk=data['r_num'])

    if clientRequest.read_check == 0:
        Request.objects.filter(pk=data['r_num']).update(read_check=2)

    Comment.objects.create(r_num=clientRequest, writer=request.session['name'], reply_value=data['comment'])

    return HttpResponse()

# 클라이언트 댓글 삭제
def deleteclientreply(request):
    
    if request.session.has_key('name'):

        Comment.objects.filter(id=request.GET['id'], writer=request.session['name']).delete()

        return HttpResponse("success")
    
    return HttpResponse("fail")

# 클라이언트 댓글 수정
@csrf_exempt
def updatereply(request):
    # Post 형식 데이터 수신
    data = request.POST

    clientComment = Comment.objects.filter(id=data['id'], writer=request.session['name'])

    value = clientComment.values()

    requestObject = Request.objects.filter(r_num=int(value[0]['r_num_id']))
        
    requestValue = requestObject.values()

    if requestValue[0]['read_check'] == 0:
        requestObject.update(read_check=2)

    clientComment.update(reply_value=data['comment'])

    return HttpResponse()

# 클라이언트 리뷰
def review(request):
    data = request.GET

    clientRequest = Request.objects.get(pk=data['r_num'])

    Review.objects.create(r_num=clientRequest, writer=request.session['name'],
                        scope=data['scope'],review_value=data['value'])

    return HttpResponse()

# 로그인 확인
def loginCheck(request):
    if request.session.has_key('name'):
        return HttpResponse("true")
    
    return HttpResponse("false")