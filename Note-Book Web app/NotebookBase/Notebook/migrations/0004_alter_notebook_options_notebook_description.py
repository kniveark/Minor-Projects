# Generated by Django 5.0.2 on 2024-02-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notebook',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='notebook',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
