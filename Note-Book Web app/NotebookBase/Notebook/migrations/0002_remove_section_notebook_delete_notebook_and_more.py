# Generated by Django 5.0.2 on 2024-02-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='notebook',
        ),
        migrations.DeleteModel(
            name='NoteBook',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
