from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    # path('library/new/', views.create, name='library-create'),
    # path('library/<int:book_id>/', views.show, name='library-show')
]