from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book,Author
from .serialisers import BookSerializer,AuthorSerializer

class BookviewsetAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AutherViewsetAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer