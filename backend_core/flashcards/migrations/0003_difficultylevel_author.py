# Generated by Django 4.1.6 on 2023-02-13 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0002_deck_is_public_flashcard_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficultylevel',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]