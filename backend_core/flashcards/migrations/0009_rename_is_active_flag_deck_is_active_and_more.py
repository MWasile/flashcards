# Generated by Django 4.1.6 on 2023-02-07 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_alter_deck_author_alter_deck_difficulty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='is_active_flag',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='flashcard',
            old_name='is_active_flag',
            new_name='is_active',
        ),
    ]
