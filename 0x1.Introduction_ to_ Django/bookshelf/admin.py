from django.contrib import admin
from .models import Book

# Customize the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list view
    list_filter = ('publication_year',)  # Filter by publication year
    search_fields = ('title', 'author')  # Add search functionality for title and author

# Register the customized Book admin
admin.site.register(Book, BookAdmin)

