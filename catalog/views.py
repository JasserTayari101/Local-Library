from django.shortcuts import render
from .models import Book,BookInstance,Author
# Create your views here.

def index(request):
    counts = [
        {'name':'Books','count':(Book.objects.all()).count()},
        {'name':'Copies','count':(BookInstance.objects.all().count() ) },
        {'name':'Copies Available','count':(BookInstance.objects.filter(status='a')).count() },
        {'name':'Authors','count':(Author.objects.all()).count()},
    ]
    return render(request,'catalog/index.html',{'counts':counts})