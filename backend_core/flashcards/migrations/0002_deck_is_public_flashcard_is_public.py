# Generated by Django 4.1.6 on 2023-02-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
