from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from . import viewsets

app_name = 'flashcards'

router = DefaultRouter()
router.register(r'decks', viewsets.DeckViewSet, basename='deck')
router.register(r'users/decks', viewsets.DeckOwnerViewSet, basename='deck_owner')
router.register(r'users/difficulties', viewsets.DifficultyLevelOwnerViewSet, basename='lvls_owner')

urlpatterns = [
    path('flashcards/', views.FlashCardView.as_view(), name='FlashCard'),
    path('flashcards/<int:pk>/', views.FlashCardItemView.as_view(), name='FlashCardDetail'),
    *router.urls
]
