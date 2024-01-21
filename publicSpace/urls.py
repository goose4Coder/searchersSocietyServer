from django.urls import path
from .views import main_page, about_us

urlpatterns = [
    path("", main_page),
    path("about/", about_us)
]