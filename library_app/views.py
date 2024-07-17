from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book, LendRecord
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import BookForm, LendForm, ReturnForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'library_app/login.html')

@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'library_app/home.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})

@login_required
def lend_book(request):
    books = Book.objects.filter(lent_to__isnull=True)
    if request.method == 'POST':
        user = request.POST['user']
        book_title = request.POST['book']
        book = Book.objects.get(title=book_title)
        book.lent_to = user
        book.is_lent = True
        book.save()
        return redirect('home')
    return render(request, 'library_app/lend_book.html', {'books': books})


@login_required
def return_book(request):
    if request.method == 'POST':
        book_title = request.POST['book']
        book = Book.objects.get(title=book_title)
        book.is_lent = False
        book.lent_to = None
        book.save()
        LendRecord.objects.filter(book=book).delete()
        return redirect('home')
    else:
        books = Book.objects.filter(is_lent=True)
        return render(request, 'library_app/return_book.html', {'books': books})

@login_required
def issued_books(request):
    books = Book.objects.filter(is_lent=True)
    return render(request, 'library_app/issued_books.html', {'books': books})




