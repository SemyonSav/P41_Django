from django.urls import path

from .views import *

urlpatterns = [
    path("", main_view, name='main'),
    path("animals/", animals_view, name='animals'),
    path("animals/<str:animal>/", animal_view, name='animal'),
]