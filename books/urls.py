from django.urls import path
from .views import booksView, createBooksView

app_name = 'books'

urlpatterns = [
    path('', booksView, name='books'),
    path('create/', createBooksView, name='create_book'),

]