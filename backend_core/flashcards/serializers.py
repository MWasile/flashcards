from rest_framework import serializers

from .models import Flashcard


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'decks', 'category', 'difficulty', 'rating', 'tags')
