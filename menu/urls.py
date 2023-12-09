from django.urls import path
from menu.views import HomeView, BlogView


urlpatterns = [
    path("blog/", BlogView.as_view(), name="blog"),
    path("", HomeView.as_view(), name="home"),
]
