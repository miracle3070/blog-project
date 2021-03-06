from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:post_id>', views.postDetail, name="postDetail"),
    path('create/', views.create, name="create"),
    path('comment/', views.comment, name="comment"),
]