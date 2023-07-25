from django.urls import path
from .views import create_book, book_list, detail, BookListView

urlpatterns = [
    path('create/', create_book, name='create_book'),
    # path('list/', book_list, name='book_list'),
    path('list/', BookListView.as_view()),
    path('detail/<int:id>', detail, name='book_detail'),
]