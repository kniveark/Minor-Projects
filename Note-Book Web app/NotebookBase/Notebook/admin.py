from django.contrib import admin

# Register your models here.

from .models import NoteBook, Section

admin.site.register(Section)
admin.site.register(NoteBook)