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
        fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class DifficultyLevelSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False, read_only=True)

    class Meta:
        model = DifficultyLevel
        fields = ('id', 'name', 'author', 'value')


class DeckSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = AuthorSerializer()
    difficulty = DifficultyLevelSerializer()

    class Meta:
        model = Deck
        fields = ('id', 'category', 'difficulty', 'rating', 'tags', 'name', 'description', 'is_public', 'author')
