from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteBookForm
# Create your views here.

def homepage(request):
    return render(request,'home/home.html')
    #return HttpResponse("Welcome to home")

def createroom(request):
    form = NoteBookForm()
    if request.method == 'POST':
        form = NoteBookForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Notebooks')


    context = {'form' : NoteBookForm}
    return render(request,'home/CreateRoom.html',context)