# Generated by Django 5.0.1 on 2024-01-17 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_flashcard', '0002_flashcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcard',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]
