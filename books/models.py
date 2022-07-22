from django.db import models

# Create your models here.
class Book(models.Model):
    genre_choices = (
        ("General Fiction", "General Fiction"),
        ("Historical Fiction", "Historical Fiction"),
        ("Fantasy", "Fantasy"),
        ("Science Fiction", "Science Fiction"),
        ("Young Adult", "Young Adult"),
        ("Memoir", "Memoir"),
        ("History", "History"),
        ("Biography", "Biography"),
    )
    # model fields
    cover = models.ImageField(upload_to="images/", verbose_name="Book Cover") 
    title = models.CharField(max_length=100, verbose_name="Book Title", help_text="ex. King of Scars")
    author = models.CharField(max_length=50, verbose_name= "Author Name", help_text="ex. Brandon Sanderson")
    genre = models.CharField(max_length=30, choices= genre_choices, verbose_name="Genre")
    description = models.TextField(verbose_name="Description")
    avg_rating = models.FloatField(verbose_name="Average Rating")
    available = models.BooleanField(default=True, verbose_name="Availalbe")
    created_at = models.DateField(auto_now_add=True, verbose_name="Created at")
    
    def __str__(self):
        return f"{self.title} by {self.author}."
    

class Library(models.Model):
    name = models.CharField(max_length=50, verbose_name="Library Name")
    manager = models.CharField(max_length=50, verbose_name="Manager")
    distance = models.PositiveIntegerField(verbose_name="Distance")
    open = models.BooleanField(default=True, verbose_name="Open")
    