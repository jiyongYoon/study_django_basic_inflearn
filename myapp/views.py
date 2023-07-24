from django.shortcuts import render, redirect
from .forms import BookForm
from myapp.models import Book
from .serializers import BookSerializer

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/create_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})


def detail(request, id):
    book = Book.objects.get(pk=id)
    print(f'Not Serializer = {book}') # Not Serializer = Book object (1)
    serializer = BookSerializer(book)
    print(f'Serializer = {serializer.data}') # Serializer = {'title': '1번책', 'author': '1번작가', 'publication_date': None, 'price': '1500.00'}