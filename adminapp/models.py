from django.db import models
# 시간 관련 라이브러리
from django.utils import timezone

# 사용자 데이터베이스
class User(models.Model):
    # 사용자 ID (PK)
    user_id = models.CharField(max_length=50, primary_key=True)
    
    # 사용자 PW
    user_pw = models.CharField(max_length=50)

    class Meta:
        # 데이터베이스 테이블 명 'users'
        db_table = 'users'

# 게시물 데이터베이스
class Request(models.Model):
    # 게시물 기본키(PK)
    r_num = models.AutoField(primary_key=True)

    # 이름
    client_name = models.CharField(max_length=50)

    # 전화번호
    client_phone = models.CharField(max_length=50)

    # 주소
    request_address = models.CharField(max_length=100)

    # 평수
    request_size = models.IntegerField()

    # 날짜
    request_date = models.DateField()

    # 청소 단계
    request_level = models.BooleanField(default=False)

    # 메모
    request_memo = models.TextField()

    # 관리자 메모
    admin_memo = models.TextField(default="")

    # 열람 비밀번호
    read_password = models.CharField(max_length=50)

    # 읽음 유무
    read_check = models.IntegerField(default=1)

    # 작성 시간
    upload_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # 데이터베이스 테이블 명 'requests'
        db_table = 'requests'

# 청소 데이터베이스
class RequestItem(models.Model):
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

    # 요청 항목(상가 청소)
    item8 = models.BooleanField(default=False)

    # 요청 항목(외벽 청소)
    item9 = models.BooleanField(default=False)

    # 요청 항목(거주 청소)
    item10 = models.BooleanField(default=False)

    # 요청 항목(특수 청소)
    item11 = models.BooleanField(default=False)

    class Meta:
        # 데이터베이스 테이블 명 'request_item'
        db_table = 'request_item'

# 시공 데이터베이스
class Construction(models.Model):
    # 게시물 기본키(FK)
    r_num = models.ForeignKey(Request, on_delete=models.CASCADE)

    # 요청 항목(마루코팅)
    item1 = models.BooleanField(default=False)

    # 요청 항목(타일코팅)
    item2 = models.BooleanField(default=False)

    # 요청 항목(나노코팅)
    item3 = models.BooleanField(default=False)

    # 요청 항목(줄눈시공)
    item4 = models.BooleanField(default=False)

    # 요청 항목(주방상판)
    item5 = models.BooleanField(default=False)

    # 요청 항목(대리석 연마)
    item6 = models.BooleanField(default=False)

    class Meta:
        # 데이터베이스 테이블 명 'constructions'
        db_table = 'constructions'

# 댓글 데이터베이스
class Comment(models.Model):
    # 게시물 기본키(FK)
    r_num = models.ForeignKey(Request, on_delete=models.CASCADE)

    # 작성자
    writer = models.CharField(max_length=50)

    # 작성 내용
    reply_value = models.TextField(null=False, blank=False)

    # 작성 시간
    reply_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # 데이터베이스 테이블 명 'comments'
        db_table = 'comments'

# 후기 데이터베이스
class Review(models.Model):
    # 게시물 기본키(FK)
    r_num = models.ForeignKey(Request, on_delete=models.CASCADE)

    # 작성자
    writer = models.CharField(max_length=50)

    # 별점
    scope = models.IntegerField(default=5)

    # 작성 내용
    review_value = models.TextField(null=False, blank=False)

    # 작성 시간
    review_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # 데이터베이스 테이블 명 'reviews'
        db_table = 'reviews'