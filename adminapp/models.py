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

class Requests(models.Model):
    # 요청사항 기본키(PK)
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

    # 요청 항목들
    

    # 열람 비밀번호
    read_password = models.CharField(max_length=50)

    # 읽음 유무
    read_check = models.IntegerField(default=0)