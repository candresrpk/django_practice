from django.urls import path
from .views import booksView, createBooksView, updateBooksView, deleteBooksView

app_name = 'books'

urlpatterns = [
    path('', booksView, name='books'),
    path('create/', createBooksView, name='create_book'),
    path('edit/<int:id>', updateBooksView, name='edit_book'),
    path('delete/<int:id>', deleteBooksView, name='delete_book'),

]