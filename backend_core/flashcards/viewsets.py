from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from . import models
from . import serializers


class DeckViewSet(ViewSet):
    queryset = models.Deck.objects.all()

    def list(self, request):
        serializer = serializers.DeckSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)