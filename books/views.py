from django.shortcuts import render


# Create your views here.

def booksView(request):
    return render(request, 'books/books.html')


def createBooksView(request):
    return render(request, 'books/crear.html')


def updateBooksView(request):
    return render(request, 'books/books.html')


def deleteBooksView(request):
    return render(request, 'books/books.html')

