from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('books',views.list_books,name='list_books'),
    path('book/<int:book_id>',views.book_detail,name='book-detail'),
    path('authors',views.list_authors,name='list_authors'),
    path('author/<int:author_id>',views.author_detail,name='author-detail'),
    path('my_books',views.user_books,name='user_books'),
]
