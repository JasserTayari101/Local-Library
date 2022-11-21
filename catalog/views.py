from django.shortcuts import render,get_object_or_404
from .models import Book,BookInstance,Author
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required #wrap around views that require login

def index(request):
    counts = [
        {'name':'Books','count':(Book.objects.all()).count()},
        {'name':'Copies','count':(BookInstance.objects.all().count() ) },
        {'name':'Copies Available','count':(BookInstance.objects.filter(status='a')).count() },
        {'name':'Authors','count':(Author.objects.all()).count()},
    ]

    visited = request.session.get('visited',False)
    if not visited:
        request.session['visited'] = True

    return render(request,'catalog/index.html',{'counts':counts,'visited':visited})


def list_books(request):
    all_books = Book.objects.all()
    #
    #paginator = Paginator(all_books,4)
    #
    #page = request.GET.get('page')
   #
    #try:
    #    books = paginator(page)
    #except PageNotAnInteger:
    #    books = paginator(1)
    #except EmptyPage:
    #    books = paginator(paginator.num_pages)
    #
    return render(request,'catalog/books.html',{'books':all_books})

def book_detail(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    copies = BookInstance.objects.filter(book_id=book_id)
    
    return render(request,f'catalog/book_detail.html',{'book':book,'copies':copies})


def list_authors(request):
    all_authors = Author.objects.all()
    
    #paginator = Paginator(all_authors,4)
   
    #page = request.GET.get('page')
   
    #try:
    #    authors = paginator(page)
    #except PageNotAnInteger:
    #    authors = paginator(1)
    #except EmptyPage:
    #    authors = paginator(paginator.num_pages)
    
    return render(request,'catalog/authors.html',{'authors':all_authors})

def author_detail(request,author_id):
    author = get_object_or_404(Author,id=author_id)
    
    if author: 
        books = Book.objects.filter(author_id=author_id)  
    
    return render(request,f'catalog/author_detail.html',{'author':author,'books':books})


@login_required
def user_books(request):
    loaned_books = BookInstance.objects.filter(borrower=request.user).filter(status='o').order_by('-due_back')

    return render(request,'catalog/user_books.html',{'loaned_books':loaned_books})