from urllib import request
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BookDetailSerializer, BookSerializer, LibrarySerializer 
from .models import Book, Library

# Create your views here.
class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDetails(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'

class LibraryList(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer