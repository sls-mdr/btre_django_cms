from django.urls import path, include

from . import views

urlpatterns = [
    path("contacts", views.contact, name="contact"),
]
