from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("compose/", views.compose, name="compose"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),

]