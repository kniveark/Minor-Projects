from django.forms import ModelForm
from Notebook.models import NoteBook

class NoteBookForm(ModelForm):
    class Meta :
        model = NoteBook
        fields = '__all__'   #['name']