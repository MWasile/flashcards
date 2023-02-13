from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .permissions import IsAuthor


class FlashCardView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FlashCardSerializer
    queryset = models.Flashcard.objects.all()

    # def get_queryset(self):
    #     rating = self.request.query_params.get('rating', None)
    #     return Flashcard.objects.filter(rating__gte=rating)


class FlashCardItemView(RetrieveUpdateDestroyAPIView):
    queryset = models.Flashcard.objects.all()
    serializer_class = serializers.FlashCardSerializer
