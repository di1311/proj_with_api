from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewHomePage.as_view(), name='home_page_url'),
    path('search/', GameDetailView.as_view(), name='search_view_url'),
    path('search/<str:internal_name>/', GameDetailView.as_view(), name='game_detail_url'),
    path('popular_games/', PopularGamesView.as_view(), name='popular_games_url'),
]
