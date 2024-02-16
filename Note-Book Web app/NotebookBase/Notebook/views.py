from django.shortcuts import render
from django.http import HttpResponse
from .models import NoteBook

# Create your views here.

def Notebooks(request):
    notebooks = NoteBook.objects.all()
    context = {'notebooks' : notebooks}
    #return HttpResponse("The list of Notebooks")
    return render(request, 'Notebook/notebooks.html',context)

def notebook(request,pk):
    #context = {'pk' : pk}
    return HttpResponse("welcome")