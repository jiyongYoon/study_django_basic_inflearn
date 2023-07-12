from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True) # 데이터 생성시 자동으로 현재 시간이 기록됨
    update_at = models.DateTimeField(auto_now=True)

