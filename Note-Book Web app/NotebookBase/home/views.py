from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'home/home.html')
    #return HttpResponse("Welcome to home")