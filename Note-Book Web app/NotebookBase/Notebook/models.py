from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteBook(models.Model):
    name = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Section(models.Model):
    notebook = models.ForeignKey(NoteBook, on_delete = models.CASCADE)
    title = models.CharField(max_length = 40)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name