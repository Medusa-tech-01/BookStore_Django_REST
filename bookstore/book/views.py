from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import *
from .serializers import *
from .forms import *
from django.contrib import messages
# Create your views here.


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {'books': books})

def add_books(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book saved successfully")
        else:
            messages.error(request, "Add Valid details")
    else:
        form = BookForm()
    return render(request, "add_books.html", {'form': form})

def update_books(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully")
            return redirect('update_books_view', pk=pk)
        else:
            messages.error(request, "Enter Valid details")
    else:
        form = BookForm(instance=book)
    return render(request, "update_books.html", {'form': form})

def delete_books(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully")
    return render(request, "delete_books.html", {'book': book})