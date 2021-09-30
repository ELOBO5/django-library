from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Book

def home(request):
    return render(request, 'library/home.html')

@login_required
def books(request):
    data = {"books": Book.objects.all()}
    return render(request, 'library/books.html')

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=id)
    data = {'book': book}   
    return render(request, 'library/show.html', data)

def not_found_404(request, execption):
    data={'err': execption}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html', data)
