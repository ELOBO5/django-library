from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse 

from .models import Book

def home(request):
    data = {"books": Book.objects.all()}
    return render(request, 'home.html')

def books(request, book_id):
    book = get_object_or_404(Book, pk=id)
    data = {'book': book}   
    return render(request, 'books.html', data)

def get_object_or_404(request, execption):
    data={'err': execption}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html', data)