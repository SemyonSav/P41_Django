from django.urls import path

from .views import *

urlpatterns = [
    path("", main_view, name='main'),
    path("add/", add_view, name='add'),
    path("delete/<int:id>/", delete_view, name='delete'),
    path("edit/<int:id>/", edit_view, name='edit'),
    path("post/add/", add_post_view, name='add_post'),
    path("posts/", posts_view, name='posts'),
    path("posts/<int:id>/", post_view, name='post'),
    path('author/<int:id>/', author_view, name='author'),
]