from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Notebooks(request):
    #return HttpResponse("The list of Notebooks")
    return render(request, 'Notebook/notebooks.html')

def notebook(request,pk):
    #context = {'pk' : pk}
    return HttpResponse("welcome")