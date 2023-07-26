from django.urls import path
# from .views import create_book, book_list, detail, BookListView
#
# urlpatterns = [
#     path('create/', create_book, name='create_book'),
#     # path('list/', book_list, name='book_list'),
#     path('list/', BookListView.as_view()),
#     path('detail/<int:id>', detail, name='book_detail'),
# ]

"""
django의 URL 디스패치 시스템 or URL 라우팅 시스템
: django urls.py 모듈에서 url에 해당하는 뷰함수나 뷰셋에 매핑하여 처리

DRF의 Router 기능
: RESTful API 구축을 위한 자동 URL 라우팅과 뷰셋 바인딩을 돕는 기능
CRUD URL 패턴을 자동으로 생성하는 메서드 제공
"""

from django.urls import include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
# r을 앞에 붙이는 이유는 정규표현식을 사용할때 사용. 일반 string도 사용 가능하기 때문에 그냥 붙임
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""
Router를 사용하지 않는다면 아래와 같이 URL에 대한 매핑작업을 해주어야 함

urlpatterns = [
    path('mymodels/', mymodels_viewset, name='mymodels-list'),
    path('mymodels/<int:pk>/', mymodel_detail_view, name='mymodels-detail'),
]

"""