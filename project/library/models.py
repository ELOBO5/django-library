from django.db import models

# Create your models here.
book_info = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} ({self.author})'