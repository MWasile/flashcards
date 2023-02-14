from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Flashcard, Deck, Tag, DifficultyLevel


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'decks', 'category', 'difficulty', 'rating', 'tags')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'id')


class DifficultyLevelSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    author = AuthorSerializer(required=False, read_only=True)

    class Meta:
        model = DifficultyLevel
        fields = ('id', 'author', 'value', 'name')

class DeckSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    difficulty = serializers.PrimaryKeyRelatedField(queryset=DifficultyLevel.objects.all())

    class Meta:
        model = Deck
        fields = ('id', 'category', 'difficulty', 'rating', 'tags', 'name', 'description', 'is_public', 'author')
