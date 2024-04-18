# Generated by Django 5.0.1 on 2024-01-18 18:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_flashcard', '0003_rename_categoria_flashcard_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashcardDesafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondido', models.BooleanField(default=False)),
                ('acertou', models.BooleanField(default=False)),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App_flashcard.flashcard')),
            ],
        ),
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('quantidade_perguntas', models.IntegerField()),
                ('dificuldade', models.CharField(choices=[('D', 'Dificil'), ('M', 'Medio'), ('F', 'Facil')], max_length=1)),
                ('categoria', models.ManyToManyField(to='App_flashcard.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('flashcards', models.ManyToManyField(to='App_flashcard.flashcarddesafio')),
            ],
        ),
    ]
