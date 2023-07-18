from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from .forms import BookForms
from django.contrib import messages

def home(request):
    options = Book.CATEGORY_OPTIONS
    categories = []
    for option in options:
        categories.append(option[1])
    
    every_books = Book.objects.order_by("-date")
    books = every_books[:10]
    
    return render(request, 'home.html', {'categories': categories, 'carousel': books})

def category(request, category_name):
    options = Book.CATEGORY_OPTIONS
    parameter = request.GET
    if parameter:
        category_name = options.filter(options__icontains=parameter)
    
    books = Book.objects.order_by("title").filter(category__icontains=category_name)
    
    categories = [" "]
    for option in options:
        categories.append(option[1])
        
    return render(request, 'category.html', {'category': category_name, 'books': books, 'categories': categories})

def search(request):
    books = Book.objects.order_by("title")
    
    if "search" in request.GET:
        title_to_search = request.GET['search']
        
        if title_to_search:
            books = books.filter(title__icontains=title_to_search)
    
    return render(request, 'search.html', {'books': books})
    
def book(request, book_id):
    info = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': info})

def indication(request):
    form = BookForms()
    
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES)
        
        if form.is_valid():
            
            title = form['title'].value()
            author = form['author'].value()
            cover = form['cover'].value()
            synopsis = form['synopsis'].value()
            category = form['category'].value()
            
            if Book.objects.filter(title=title.title()).exists():
                messages.error(request, "Desculpe, esse livro já foi indicado!")
                return redirect('indication')
            
            book = Book(
                title=title.title(),
                author=author.title(),
                cover=cover,
                synopsis=synopsis,
                category=category
            )
           
            book.save()
            return redirect('home')

    return render(request, 'form.html', {'form': form})