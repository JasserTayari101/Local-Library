from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    """Model representing a book genre"""
    
    name = models.CharField(max_length=200,help_text="Enter a book genre(e.g. Science Fiction)")
    
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    """Model representing a book(but not a specific copyp"""
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True,related_name='author')
    summury = models.TextField(max_length=1000,help_text="Enter a brief description of the book")
    isbn = models.CharField(max_length=13,unique=True)
    genre = models.ManyToManyField(Genre,help_text="Select genres for this book")
    
    
    def __str__(self):
        return f'{self.title} written by {self.author.name}'
    
    def get_absolute_url(self):
        return reverse("book-detail",args=[
            str(self.id)
        ])
        
class BookInstance(models.Model):
    """Model representing a unique instance of a book"""

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'), 
        ('a','Available'),
        ('r','Reserved') 
    )

    unique_id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique ID for this book accross the library")
    due_back = models.DateField(null=True,blank=True)
    status = models.CharField(choices=LOAN_STATUS,max_length=1,default='a',blank=True,help_text="Book Availability")
    book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True,related_name="book")
    imprint = models.CharField(max_length=200)
   
    class Meta:
        ordering = ('due_back','status') 
    
    def __str__(self):
        return f'{self.unique_id} ({self.book.title})'
    

class Author(models.Model):
    """Model representing an author"""

    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)
    
    class Meta:
        ordering = ('name','-date_of_birth')
    
    def get_absolute_url(self):
        return reverse("author-detail",args=[str(self.id)])
    
    def __str__(self):
        return self.name
    