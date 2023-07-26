from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Book
from .serializers import BookSerializer


# Create your tests here.
class BookTests(TestCase):

    # BeforeEach와 같음 // AfterEach는 tearDown()으로 사용할 수 있음.
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "test book",
            "author": "test author",
            "publication_date": "2019-08-24",
            "price": "1234.56"
        }
        self.book = Book.objects.create(**self.book_data) # **는 딕셔너리 형태로 함수에 전달하는 것.
        # Book.objects.create(title="test book", author="test author", publication_date="2019-08-24", price="1234.56")

    def test_get_all_books(self):
        response = self.client.get('/myapp/books/')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)  # Check 'results' key

    def test_get_single_book(self):
        response = self.client.get(f'/myapp/books/{self.book.id}/')
        book = Book.objects.get(id=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        response = self.client.post('/myapp/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Book',
            'author': 'Jane Smith',
            'publication_date': '2023-02-01',
            'price': '19.99',  # Updated to a string value
        }
        response = self.client.put(f'/myapp/books/{self.book.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, updated_data['title'])
        self.assertEqual(updated_book.author, updated_data['author'])
        self.assertEqual(updated_book.publication_date.strftime('%Y-%m-%d'), updated_data['publication_date'])
        self.assertEqual(str(updated_book.price), updated_data['price'])  # Convert Decimal to string

    def test_delete_book(self):
        response = self.client.delete(f'/myapp/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

"""
실행 로그를 보면 test db를 만들어서 실행한다
test DB를 만들어서 api 요청 및 응답을 하고, test가 종료되면 DB는 자동으로 삭제된다.
"""