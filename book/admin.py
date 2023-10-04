from django.contrib import admin
from book.models import Book, Contact, Customer

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'book_title', 'book_author', 'book_price', 'book_desc', 'book_pub_date', 'book_image')

admin.site.register(Book, BookAdmin)
# Register your models here.
