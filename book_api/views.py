from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_api.models import Book
from book_api.serializer import BookSerializer


@api_view(["GET"])
def book_list(request):
    books = BookSerializer(Book.objects.all(), many=True)
    return Response(books.data)

@api_view(["POST"])
def book_create(request):
    book = BookSerializer(data=request.data)
    if book.is_valid():
        book.save()
        return Response(book.data)
    return Response(book.errors)
