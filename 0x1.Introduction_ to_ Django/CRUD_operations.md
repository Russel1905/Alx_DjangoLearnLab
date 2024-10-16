from bookshelf.models import Book

# Create a new book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)


# Retrieve the book
book = Book.objects.get(pk=1)  

# Update the book
book.title = "Nineteen Eighty-Four"
book.save()

# Delete the book
book.delete()
book.objects.all()