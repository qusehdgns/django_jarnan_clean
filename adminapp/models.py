from django.db import models

# 사용자 데이터베이스
class User(models.Model):
    # 사용자 ID (PK)
    user_id = models.CharField(max_length=50, primary_key=True)
    
    # 사용자 PW
    user_pw = models.CharField(max_length=50)

    class Meta:
        # 데이터베이스 테이블 명 'users'
        db_table = 'users'

class Request(models.Model):
    # 게시물 기본키(PK)
    r_num = models.AutoField(primary_key=True)

    # 이름
    client_name = models.CharField(max_length=50)

    # 전화번호
    client_phone = models.CharField(max_length=50)

    # 주소
    client_address = models.CharField(max_length=100)

    # 날짜
    request_date = models.DateField()

    # 평수
    request_size = models.IntegerField()

    # 메모
    request_memo = models.TextField()

    # 열람 비밀번호
    read_password = models.CharField(max_length=50)

    # 읽음 유무
    read_check = models.IntegerField(default=0)

    class Meta:
        # 데이터베이스 테이블 명 'users'
        db_table = 'requests'

class RequestItems(models.Model):
    # 게시물 기본키(FK)
    r_num = models.ForeignKey(Request, on_delete=models.CASCADE)

    # 요청 항목(입주 청소)
    item1 = models.BooleanField(default=False)

    # 요청 항목(이사 청소)
    item2 = models.BooleanField(default=False)

    # 요청 항목(인테리어 후 청소)
    item3 = models.BooleanField(default=False)

    # 요청 항목(사무실 청소)
    item4 = models.BooleanField(default=False)

    # 요청 항목(식당 청소)
    item5 = models.BooleanField(default=False)

    # 요청 항목(준공 청소)
    item6 = models.BooleanField(default=False)

    # 요청 항목(학교 청소)
    item7 = models.BooleanField(default=False)

    # 요청 항목(관공서 청소)
    item8 = models.BooleanField(default=False)

    class Meta:
        # 데이터베이스 테이블 명 'users'
        db_table = 'request_items'