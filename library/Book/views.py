from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
