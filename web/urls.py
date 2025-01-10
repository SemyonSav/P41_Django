from django.urls import path

from .views import *

urlpatterns = [
    path("", main_view, name='main'),
    path("register/", register_view, name='register'),
    path("auth/", auth_view, name='auth'),
    path("logout/", logout_view, name='logout'),
    path("books/", books_view, name='books')
]