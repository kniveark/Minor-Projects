from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.homepage, name="Homepage"),
    path('create-notebook/',views.createbook, name = "create-book"),
    path('update-notebook/<str:pk>',views.updatebook, name = "update-book"),

]
