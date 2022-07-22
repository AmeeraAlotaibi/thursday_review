from rest_framework import serializers
from .models import Book, Library

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "avg_rating", "created_at"]

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ["id", "cover", "title", "author", "genre", "avg_rating", "description", "available", "created_at", ]

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"