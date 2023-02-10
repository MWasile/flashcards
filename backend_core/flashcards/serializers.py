from rest_framework import serializers

from .models import Flashcard, Deck


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'decks', 'category', 'difficulty', 'rating', 'tags')


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'category', 'difficulty', 'rating', 'tags', 'name', 'description', 'is_public', 'author')
