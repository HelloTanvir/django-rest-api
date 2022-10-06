from django.contrib import admin
from django.urls import path

from book_api.views import book_create, book_list

urlpatterns = [
    path("list/", book_list),
    path("", book_create),
]
