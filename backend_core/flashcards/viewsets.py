from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from . import models, paginations
from . import serializers
from .permissions import IsAuthor


class DeckViewSet(ModelViewSet):
    queryset = models.Deck.objects.select_related('difficulty', 'author').prefetch_related('tags').all()
    pagination_class = paginations.CustomPaginator
    serializer_class = serializers.DeckSerializer

    def list(self, request, *args, **kwargs):
        # serializer = serializers.DeckSerializer(self.queryset, many=True)
        # return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)


class DeckOwnerViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = models.Deck.objects.all()

    def list(self, request):
        decks = self.queryset.filter(author=request.user)
        serializer = serializers.DeckSerializer(decks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        deck = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, deck)
        serializer = serializers.DeckSerializer(deck)
        return Response(serializer.data)


class DifficultyLevelOwnerViewSet(ModelViewSet):
    allowed_methods = ['GET', 'POST', 'PATCH']
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = models.DifficultyLevel.objects.all()

    def list(self, request, *args, **kwargs):
        levels = self.queryset.filter(author=request.user)
        serializer = serializers.DifficultyLevelSerializer(levels, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        level = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, level)
        serializer = serializers.DifficultyLevelSerializer(level)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.DifficultyLevelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data)

    def update(self, request, *args, pk=None, **kwargs):
        level = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, level)
        serializer = serializers.DifficultyLevelSerializer(level, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, pk=None, **kwargs):
        level = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, level)
        serializer = serializers.DifficultyLevelSerializer(level, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, pk=None, **kwargs):
        level = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, level)
        level.delete()
        return Response(status=204)


class TagOwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = models.Tag.objects.all()

    def list(self, request, *args, **kwargs):
        tags = self.queryset.filter(author=request.user)
        serializer = serializers.TagSerializer(tags, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        tag = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, tag)
        serializer = serializers.TagSerializer(tag)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data)

    def update(self, request, *args, pk=None, **kwargs):
        tag = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, tag)
        serializer = serializers.TagSerializer(tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        tag = get_object_or_404(queryset=self.queryset, pk=pk)
        self.check_object_permissions(request, tag)
        tag.delete()
        return Response(status=204)