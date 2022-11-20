from django.shortcuts import render
from .models import Book,BookInstance,Author
# Create your views here.

def index(request):
    counts = [
        {'name':'Books','count':len(Book.objects.all() )},
        {'name':'Copies','count':len(BookInstance.objects.all() ) },
        {'name':'Copies Available','count':len(BookInstance.objects.filter(status='a')) },
        {'name':'Authors','count':len(Author.objects.all())},
    ]
    return render(request,'catalog/index.html',{'counts':counts})