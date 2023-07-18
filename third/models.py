from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True) # 이 필드가 새로 추가되는 것이기 때문에, default 값을 설정해주지 않으면 기존에 입력되어있던 Data 값이 없기 때문에
    image = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) # ManyToOne

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)