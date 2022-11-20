from django.shortcuts import render,get_object_or_404
from .models import Book,BookInstance,Author
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def index(request):
    counts = [
        {'name':'Books','count':(Book.objects.all()).count()},
        {'name':'Copies','count':(BookInstance.objects.all().count() ) },
        {'name':'Copies Available','count':(BookInstance.objects.filter(status='a')).count() },
        {'name':'Authors','count':(Author.objects.all()).count()},
    ]
    return render(request,'catalog/index.html',{'counts':counts})


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