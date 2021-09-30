from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('books/', views.show, name='library-book'),
    path('books/<int:book_id>/', views.show, name='book-show')
]