from django.urls import path
from .views import *



urlpatterns = [
    path('', ViewHomePage.as_view(), name='home_page_url'),
    path('search/', ViewResponse.as_view(), name='search_view_url'),
    path('search/<str:id>_<str:deal_id>', GameDetailView.as_view(), name='game_detail_url'),
]

