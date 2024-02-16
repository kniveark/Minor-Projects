from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.homepage, name="Homepage"),
    path('create-notebook/',views.createroom, name = "create-room"),
]
