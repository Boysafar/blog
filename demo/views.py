from django.shortcuts import render
from .models import Author, Book, CompanyInfo


from django.shortcuts import render
from .models import Book, CompanyInfo


def books_page(request):
    books = Book.objects.all()
    company_info = CompanyInfo.objects.first()  # Assuming there's only one company info record
    return render(request, 'books.html', {'books': books, 'company_info': company_info})
