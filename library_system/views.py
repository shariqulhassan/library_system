from django.shortcuts import render, redirect
from .models import Book, Category
from django.db.models import Q

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'library_system/book_list.html', {'books': books, 'categories': categories})

def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if not book.borrowed:
        book.borrowed = True
        book.save()
    return redirect('book_list')

def return_book(request, id):
    book = Book.objects.get(id=id)
    if book.borrowed:
        book.borrowed = False
        book.save()
    return redirect('book_list')

def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    books = Book.objects.filter(category=category)
    return render(request, 'library_system/category_view.html', {'category': category, 'books': books})
