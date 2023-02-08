from rest_framework.generics import ListAPIView

from .models import FlashCard
from .serializers import FlashCardSerializer


class FlashCardView(ListAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
