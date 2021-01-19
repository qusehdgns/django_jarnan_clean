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
# math 사용
import math
# queryset OR 사용
from django.db.models import Q

# 데이터베이스
from adminapp.models import User, Request, RequestItem, Construction, Comment, Review

clean = ['입주 청소', '이사 청소', '인테리어 후 청소', '사무실 청소', '식당 청소',
         '준공 청소', '학교 청소', '관공서 청소', '외벽 청소', '거주 청소', '계단 청소', '특수 청소']
construct = ['마루코팅', '타일코팅', '나노코팅', '주방상판', '대리석연마']


@csrf_exempt
def admin_request_list_call(request):

    if request.session.has_key('name') == False:
        # 로그인 기록이 없을 경우
        return redirect('login_call')

    if request.GET:
        
        select = request.GET['select']

        if select == "review":
            reviews = Review.objects.all().order_by('-review_date').values();

            reviewData = []

            for temp in reviews:
                reviewData.append(temp)
            return render(request, 'Admin_Review.html', { "data" : reviewData })

        if "sort" not in request.GET:
            return redirect("/admin/request_list?select=all&page=1&sort=base")

        sort = request.GET['sort']


        if sort == "base":
            sorting = '-upload_date'
        elif sort == "where":
            sorting = 'request_address'
        elif sort == "when":
            sorting = '-request_date'
        else:
            return redirect("/admin/request_list?select=all&page=1&sort=base")

        if "page" in request.GET:
            page = int(request.GET['page'])
        else:
            page = 1

        requestList = []

        requestObject = Request.objects
        
        filtering = {}

        if request.POST:

            if "selectClean" in request.POST:
                selectClean = request.POST['selectClean'].split(',')

                filtering['selectClean'] = selectClean

                cleanBool = [False for i in range(12)]

                for temp in selectClean:
                    cleanBool[clean.index(temp)] = True

                requestItem = RequestItem.objects

                for index, temp in enumerate(cleanBool, start=1):
                    if temp:
                        col = "item" + str(index)
                        requestItem = requestItem.filter(**{col:True})

                if len(requestItem) != 0:
                    q = Q()

                    for temp in requestItem.values('r_num_id'):
                        q.add(Q(r_num=temp['r_num_id']), q.OR)

                    requestObject = requestObject.filter(q)
                else:
                    requestObject = requestObject.filter(r_num=-1)

            if "selectConstruct" in request.POST:
                selectConstruct = request.POST['selectConstruct'].split(',')

                filtering['selectConstruct'] = selectConstruct

                cunstructBool = [False for i in range(5)]

                for temp in selectConstruct:
                    cunstructBool[construct.index(temp)] = True

                requestConstruct = Construction.objects

                for index, temp in enumerate(cunstructBool, start=1):
                    if temp:
                        col = "item" + str(index)
                        requestConstruct = requestConstruct.filter(**{col:True})

                if len(requestConstruct) != 0:
                    q = Q()

                    for temp in requestConstruct.values('r_num_id'):
                        q.add(Q(r_num=temp['r_num_id']), q.OR)

                    requestObject = requestObject.filter(q)
                else:
                    requestObject = requestObject.filter(r_num=-1)

            if "startDate" in request.POST:
                startDate = request.POST['startDate']

                filtering['startDate'] = startDate

                requestObject = requestObject.filter(request_date__gte=startDate)

            if "endDate" in request.POST:
                endDate = request.POST['endDate']

                filtering['endDate'] = endDate

                requestObject = requestObject.filter(request_date__lte=endDate)

        if select == "all":
            requestData = requestObject.all().order_by(sorting, '-upload_date').values()

        elif select == "new":
            requestData = requestObject.filter(
                read_check=1).order_by(sorting, '-upload_date').values()

        elif select == "reply":
            requestData = requestObject.filter(
                read_check=2).order_by(sorting, '-upload_date').values()

        elif select == "checked":
            requestData = requestObject.filter(
                read_check=0).order_by(sorting, '-upload_date').values()

        else:
            return redirect("/admin/request_list?select=all&page=1&sort=base")

        endpage = math.ceil(len(requestData) / 10)

        if endpage == 0:
            endpage = 1

        if page > endpage or page < 1:
            return redirect("/admin/request_list?select=all&page=1&sort=base")

        start_index = (page - 1) * 10

        end_index = page * 10

        for temp in requestData[start_index:end_index]:
            requestList.append(temp)

        return render(request, 'Admin_Request_List.html',
                      {'requestList': enumerate(requestList, start=1),
                       'page': page, 'endpage': endpage,
                       "clean": clean, "construct": construct, "filtering" : filtering })

    return redirect("/admin/request_list?select=all&page=1&sort=base")


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

    Comment.objects.create(
        r_num=adminRequest, writer='잘나가는 청소', reply_value=data['comment'])

    return HttpResponse()

# 관리자 메모 수정
def updateadminmemo(request):

    requestFocus = Request.objects.filter(r_num=request.GET['r_num'])

    requestFocus.update(admin_memo=request.GET['adminMemo'])

    return HttpResponse()


# 리뷰 삭제
def deletereview(request):

    reviewId = request.GET['id']

    Review.objects.get(pk=reviewId).delete()

    return HttpResponse()