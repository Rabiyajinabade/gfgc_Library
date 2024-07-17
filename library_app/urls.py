from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('lend/', views.lend_book, name='lend_book'),
    path('return/', views.return_book, name='return_book'),
    path('issued/', views.issued_books, name='issued_books'),
]
