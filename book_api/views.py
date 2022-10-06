from django.http import JsonResponse
from django.shortcuts import render

from book_api.models import Book


def book_list(request):
    books = list(Book.objects.all().values())
    
    return JsonResponse({
        'books': books
    })
