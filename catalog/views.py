from django.shortcuts import render,get_object_or_404
from .models import Book,BookInstance,Author
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required #wrap around views that require login
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import reverse
from .forms import BorrowForm


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
    return render(request,'catalog/books.html',{'books':all_books})

def book_detail(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    copies = BookInstance.objects.filter(book_id=book_id)
    
    return render(request,f'catalog/book_detail.html',{'book':book,'copies':copies})


def list_authors(request):
    all_authors = Author.objects.all()
   
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

    
@login_required
def borrow_book(request,unique_id):
    copie = get_object_or_404(BookInstance,unique_id=unique_id)
    
    if copie.status == 'a':
        borrowed = None
        if request.method == 'POST':
            borrow_form = BorrowForm(request.POST)
            if borrow_form.is_valid():
                cd = borrow_form.cleaned_data
                copie.due_back = cd['due_back']
                copie.borrower = request.user
                copie.status = 'o'
                copie.save()
                borrowed = True
            else:
                borrow_form = BorrowForm()
        else:
            borrow_form = BorrowForm()

        return render(request,'catalog/borrow_book.html',{'borrow_form':borrow_form,'borrowed':borrowed,'copie':copie})
        
    else:
        return HttpResponse(f"This copie is not available! Can't borrow it! return at {copie.due_back}")