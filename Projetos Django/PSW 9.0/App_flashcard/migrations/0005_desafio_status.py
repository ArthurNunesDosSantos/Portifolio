# Generated by Django 5.0.1 on 2024-01-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_flashcard', '0004_flashcarddesafio_desafio'),
    ]

    operations = [
        migrations.AddField(
            model_name='desafio',
            name='status',
            field=models.CharField(default='encerrado', max_length=50),
        ),
    ]