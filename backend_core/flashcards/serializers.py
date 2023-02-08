from rest_framework import serializers import ModelSerializer

from .models import FlashCard

class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('id', 'question', 'answer', 'decks', 'category', 'difficulty', 'rating', 'tags')