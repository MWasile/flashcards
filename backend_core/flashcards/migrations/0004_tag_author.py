# Generated by Django 4.1.6 on 2023-02-14 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0003_difficultylevel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
