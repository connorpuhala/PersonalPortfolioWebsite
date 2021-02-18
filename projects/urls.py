from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("about", views.about_page, name="about_page"),
    path("story", views.story, name="story"),
]
