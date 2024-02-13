from django.urls import path
from . import views
urlpatterns = [
    path('',views.Notebooks, name='Notebooks'),
    path('<str:pk>',views.notebook,name = 'notebook')
]