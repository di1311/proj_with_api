from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewHomePage.as_view(), name='home_page_url'),
    path('search/', GameDetailView().search_games, name='search_view_url'),
    path('search/<str:internalName>', GameDetailView.as_view(), name='game_detail_url'),
    path('popular_games/', PopularGamesView().popular_games_view, name='popular_games_url'),
    path('popular_games/<str:internalName>', PopularGamesView.as_view(), name='popular_game_url')
]
