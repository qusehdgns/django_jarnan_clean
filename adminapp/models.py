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
    # 요청사항 기본키
    r_num = models.AutoField(primary_key=True)