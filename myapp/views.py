from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListAPIView

# Create your views here.
# def create_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'myapp/create_book.html', {'form': form})
#
#
# # Springboot의 RestController 비슷한 느낌쓰. 함수 기반의 API 뷰에 사용됨.
# # 뷰 함수에 대해 지원되는 HTTP 메소드를 지정하고 뷰의 요청/응답 처리를 Response로 제공함.
# @api_view(['POST'])
# def create_book(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)
#
#
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'myapp/book_list.html', {'books': books})


# ListAPIView를 상속하면 DRF 직렬화기로 보이는것 같음 (django-ListView 상속 시 기존처럼 보임)
# class BookListView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     template_name = 'myapp/book_list.html'
#
#
# def detail(request, id):
#     book = Book.objects.get(pk=id)
#     print(f'Not Serializer = {book}') # Not Serializer = Book object (1)
#     serializer = BookSerializer(book)
#     print(f'Serializer = {serializer.data}') # Serializer = {'title': '1번책', 'author': '1번작가', 'publication_date': None, 'price': '1500.00'}



## ViewSet
from rest_framework import viewsets

# 복잡한 ViewSet
# class BookViewSet(viewsets.ViewSet):
#     # [GET] /api/books/
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     # [GET] /api/books/{id}
#     def retrieve(self, request, id=None):
#         book = Book.objects.get(pk=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#
#     def mark_as_read(self, request, id=None):
#         book = Book.objects.get(pk=id)
#         book.mark_as_read()
#         return Response({'status': 'book marked as read'})

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters

from .pagination import CustomPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

page = openapi.Parameter('page', openapi.IN_QUERY, default=1, description="페이지 번호", type=openapi.TYPE_INTEGER)
size = openapi.Parameter('size', openapi.IN_QUERY, default=5, description="한 페이지에 표시할 객체 수", type=openapi.TYPE_INTEGER)


# CRUD를 포함한 ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # 사용하려면 api 요청 시 url 예시: GET http://localhost:8000/myapp/books/?ordering=-price&search=번책
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price'] # price 정렬 활성화
    search_fields = ['title'] # title 검색 활성화
    # 커스텀 pagination 클래스 설정
    pagination_class = CustomPagination

    # @swagger_auto_schema(
    #     operation_description="Get a list of books.",
    #     responses={200: BookSerializer(many=True)},
    #     tags=['Books'],  # 해당 API를 'Books' 태그로 그룹화합니다
    #     manual_parameters=[
    #         openapi.Parameter('title', openapi.IN_QUERY, description="Search by title", type=openapi.TYPE_STRING),
    #         openapi.Parameter('ordering', openapi.IN_QUERY, description="Ordering by price", type=openapi.TYPE_STRING),
    #     ],
    # )
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # action 데코레이터 -> 기본 CRUD(Create, Retrieve, Update, Delete) 작업으로 제공되지 않는 사용자 정의 작업 또는 추가적인 엔드포인트를 정의하는 데 사용
    # 기본적으로 DRF의 뷰셋은 list, retrieve, create, update, destroy와 같은 작업을 제공하며, 이는 표준 HTTP 메소드(GET, POST, PUT, DELETE)에 해당
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, id=None):
        book = self.get_object()
        book.mark_as_read()
        return Response({'status': 'book marked as read'})