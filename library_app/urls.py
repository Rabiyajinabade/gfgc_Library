from django.urls import path
from . import views
from .views import login_view, home, add_book, lend_book, return_book, issued_books, logout_view


urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('lend/', views.lend_book, name='lend_book'),
    path('return/', views.return_book, name='return_book'),
    path('issued/', views.issued_books, name='issued_books'),
    path('logout/', logout_view, name='logout'),
]
