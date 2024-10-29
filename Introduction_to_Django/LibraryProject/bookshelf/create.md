# Detailed CRUD Operations and Documentation

## Create
**Command:** Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# No output is shown upon successful creation, but the instance is saved in the database.
