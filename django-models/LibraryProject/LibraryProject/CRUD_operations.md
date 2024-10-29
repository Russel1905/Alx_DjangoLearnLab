# CRUD Operations for Book Model

This document outlines the CRUD operations performed on the Book model within the Django shell.

## Create Operation
To create a new book instance, run the following command:

```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

##RETRIEVE OPERATION
all_books = Book.objects.all()
print(all_books)
 #EXPECTED OUTPUT
 <QuerySet [<Book: 1984>]>

#UPDATE
book.title = "Nineteen Eighty-Four"
book.save()

#OUTPUT
# No output is shown upon successful update, but the instance's title is updated in the database.

#DELETE
book.delete()

#EXPECTATION
(1, {'bookshelf.Book': 1})  # Indicates that one Book instance was deleted.
