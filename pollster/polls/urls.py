from django.urls import path
from . import views

app_name = "Polls"

urlpatterns= [
    path("", views.index, name="index")
]