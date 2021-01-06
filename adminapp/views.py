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

# 데이터베이스
from adminapp.models import User, Request, RequestItem, Construction, Comment

clean = ['입주 청소', '이사 청소', '인테리어 후 청소', '사무실 청소', '식당 청소',
         '준공 청소', '학교 청소', '관공서 청소', '외벽 청소', '거주 청소', '계단 청소', '특수 청소']
construct = ['마루코팅', '타일코팅', '나노코팅', '주방상판', '대리석연마']


def admin_request_list_call(request):

    if request.session.has_key('name') == False:
        # 로그인 기록이 없을 경우
        return redirect('login_call')

    if request.GET:

        requestList = []

        requestObject = Request.objects

        select = request.GET['select']

        if select == "all":
            requestData = requestObject.all().order_by('-upload_date').values()

        elif select == "new":
            requestData = requestObject.filter(
                read_check=1).order_by('-upload_date').values()

        elif select == "reply":
            requestData = requestObject.filter(
                read_check=2).order_by('upload_date').values()

        elif select == "checked":
            requestData = requestObject.filter(
                read_check=0).order_by('-upload_date').values()

        else:
            return redirect("/admin/request_list?select=all")

        for temp in requestData:
            requestList.append(temp)

        return render(request, 'Admin_Request_List.html',
                      {'requestList': enumerate(requestList, start=1)})

    return redirect("/admin/request_list?select=all")


# 요청 확인 페이지
def admin_request_call(request):

    Request.objects.filter(r_num=request.GET['r_num']).update(read_check=0)

    clientRequest = Request.objects.get(pk=request.GET['r_num'])

    items = RequestItem.objects.filter(r_num=clientRequest).values()

    cleanItems = []

    for data in items:
        for index, value in enumerate(clean, start=1):
            temp = {"clean": value, "value": data['item' + str(index)]}
            cleanItems.append(temp)

    constructs = Construction.objects.filter(r_num=clientRequest).values()

    constructions = []

    for data in constructs:
        for index, value in enumerate(construct, start=1):
            temp = {"construct": value, "value": data['item' + str(index)]}
            constructions.append(temp)

    comments = Comment.objects.filter(
        r_num=clientRequest).order_by("reply_date").values()

    replys = []

    for data in comments:
        temp = {'id': data['id'], 'writer': data['writer'],
                'reply_value': data['reply_value']}
        replys.append(temp)

    return render(request, "Admin_Request.html",
                  {"request": clientRequest, "items": enumerate(cleanItems),
                   "constructs": enumerate(constructions), 'comments': replys})


# 댓글 삭제
def deletereply(request):

    Comment.objects.filter(id=request.GET['id']).delete()

    return HttpResponse("success")

# 댓글 수정
@csrf_exempt
def updatecomment(request):
    # Post 형식 데이터 수신
    data = request.POST

    adminComment = Comment.objects.filter(id=data['id'])

    adminComment.update(reply_value=data['comment'])

    return HttpResponse()

# 댓글 달기
@csrf_exempt
def adminreply(request):
    # Post 형식 데이터 수신
    data = request.POST

    adminRequest = Request.objects.get(pk=data['r_num'])

    Comment.objects.create(r_num=adminRequest, writer='잘나가는 청소', reply_value=data['comment'])

    return HttpResponse()

# 관리자 메모 수정
def updateadminmemo(request):

    requestFocus = Request.objects.filter(r_num=request.GET['r_num'])

    requestFocus.update(admin_memo=request.GET['adminMemo'])

    return HttpResponse()