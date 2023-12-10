from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm

# Create your views here.

def booksView(request):

    data = Book.objects.all()

    context = {
        'books' : data
    }

    return render(request, 'books/books.html', context)


def createBooksView(request):

    formulario = BookForm(request.POST or None, request.FILES or None)

    context = {
        'form': formulario
    }

    if formulario.is_valid():
        formulario.save()

        return redirect ('books:books')
    

    return render(request, 'books/crear.html', context)


def updateBooksView(request, id):

    book = Book.objects.get(id=id)

    formulario = BookForm(
        request.POST or None, 
        request.FILES or None, 
        instance=book
    )

    context = {
        'form': formulario
    }

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('books:books')


    return render(request, 'books/editar.html', context)


def deleteBooksView(request, id):

    book = Book.objects.get(id=id)
    book.delete()

    return redirect('books:books')

