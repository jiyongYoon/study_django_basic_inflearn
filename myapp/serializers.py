from rest_framework import serializers
from .models import Book

from datetime import datetime

# ModelSerializer 클래스는 모델 인스턴스와 쿼리셋을 다루는 시리얼라이저를 생성하기 위한 단축키 역할을 함.
# Django 모델의 필드와 일치하는 필드를 자동으로 생성함.
class BookSerializer(serializers.ModelSerializer):
    # 현재 날짜가 직렬화가 안되고 있음... (23/07/25)
    # publication_date = serializers.SerializerMethodField()

    # 직렬화에 포함시키고자 하는 모델과 필드정보 추가
    class Meta:
        model = Book
        # fields = ['title', 'author', 'publication_date', 'price']
        fields = '__all__'


    # Django REST framework의 SerializerMethodField 사용 시, 메서드 이름을 {get_<필드명>} 으로 해야 동작함.
    def get_publication_date(self, obj):
        return timestamp_to_datetime(obj.publication_date)


def timestamp_to_datetime(timestamp):
    # 10자리인 경우 (초 단위)
    if len(str(timestamp)) == 10:
        return datetime.fromtimestamp(timestamp)
    # 13자리인 경우 (밀리초 단위)
    elif len(str(timestamp)) == 13:
        return datetime.fromtimestamp(timestamp / 1000)
    else:
        raise ValueError("Invalid timestamp format.")

    """ 사용
    book = Book.objects.get(pk=1)
    serializer = BookSerializer(book)
    print(serializer.data)
    """

"""
만약 관련 모델에 대한 중첩된 시리얼라이저 작업을 하는 경우

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'nationality']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer() <- 이렇게 추가해줌

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price']

"""

# django에서 기본적으로 제공하는 인증 관련 테이블인 auth_user 테이블
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
