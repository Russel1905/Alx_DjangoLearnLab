from django.urls import path
from .views import list_books, LibraryDetailView
from .views import user_login, user_logout, register
from .views import (
    list_books, 
    LibraryDetailView, 
    user_login, 
    user_logout, 
    register,
    admin_view, 
    librarian_view, 
    member_view,
    add_book,edit_book,
    delete_book
)


urlpatterns = []

urlpatterns += [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]

urlpatterns += [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
# relationship_app/urls.py
urlpatterns += [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
# relationship_app/urls.py
urlpatterns += [
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]

