from django.contrib import admin
from .models import Book,BookInstance,Author,Genre,Language




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    list_filter = ('genres','languages')
    search_fields = ('summary',)
    raw_id_fields = ('genres','languages')
    



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('unique_id','book','status','due_back','borrower')
    list_filter = ('status','book','due_back')
    search_fields = ('imprint',)
    raw_id_fields = ('book',)


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)