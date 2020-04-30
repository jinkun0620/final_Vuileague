from django.db import models
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    #팀 이름 받기
    teamname = models.CharField(max_length=64)
    #사용자 프로필
    profile_photo = models.FileField(null=True, blank=True)
    CITY = ((1,'Hanoi'),(2,'TP HCM'))
    #도시 위치
    city = models.IntegerField(choices=CITY, default=1,)
    HOME = ((1,'D1'),(2,'D2'),(3,'D3'),(4,'D4'),(5,'D5'),(6,'D6'),(6,'D6'),(7,'D7'))
    # 홈구장
    home = models.IntegerField(choices=HOME, default=1,)
    #소개
    introduce = models.TextField()
    # 몇 대 몇?
    member = models.CharField(max_length=20)
    #일자 등록
    made_on = models.DateField(default=timezone.now)
    #예약일자
    book = models.DateTimeField(default=timezone.now)
    #게시글 생성 일자
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self): 
        return self.teamname

class Match(models.Model):
    # 주소 City/Province

    HOME = ((1,'D1'),(2,'D2'),(3,'D3'),(4,'D4'),(5,'D5'),(6,'D6'),(6,'D6'),(7,'D7'))
    # 주소 Ward
    home = models.IntegerField(choices=HOME, default=1,)
    #소개
    MEMBER = ((1,'5 vs 5/ 6 vs 6'),(2,'7 vs 7/ 8 vs 8'),(3,'11 vs 11'))
    member = models.IntegerField(choices=MEMBER, default=1,)
    #일자 등록
    made_on = models.DateField(default=timezone.now)
    #예약일자
    book = models.DateTimeField(default=timezone.now)
    #게시글 생성 일자
    created_date = models.DateTimeField(default=timezone.now)