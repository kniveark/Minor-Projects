from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteBookForm
from Notebook.models import NoteBook
# Create your views here.

def homepage(request):
    return render(request,'home/home.html')
    #return HttpResponse("Welcome to home")

def createbook(request):
    form = NoteBookForm()
    if request.method == 'POST':
        form = NoteBookForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Notebooks')


    context = {'form' : NoteBookForm}
    return render(request,'home/CreateBook.html',context)

def updatebook(request,pk):
    bookobj = NoteBook.objects.get(id = pk)
    form = NoteBookForm(instance=bookobj)
    
    if request.method == 'POST':
        form = NoteBookForm(request.POST, instance = bookobj )
        if form.is_valid:
            form.save()
            return redirect('Notebooks')
        
    context = {'form' : form}
    return render(request, 'home/UpdateBook.html', context)