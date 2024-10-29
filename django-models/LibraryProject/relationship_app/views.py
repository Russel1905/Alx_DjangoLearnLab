
from django.shortcuts import render
from .models import Book, Library
from django.views import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Add book logic here
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # Edit book logic here
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # Delete book logic here
    pass


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    # Admin view logic here
    pass

@user_passes_test(is_librarian)
def librarian_view(request):
    # Librarian view logic here
    pass

@user_passes_test(is_member)
def member_view(request):
    # Member view logic here
    pass


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

