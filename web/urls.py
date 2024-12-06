from django.urls import path

from .views import *

urlpatterns = [
    path("", main_view, name='main'),
    path("add/", add_view, name='add'),
    path("delete/<int:id>/", delete_view, name='delete'),
    path("edit/<int:id>/", edit_view, name='edit')
]