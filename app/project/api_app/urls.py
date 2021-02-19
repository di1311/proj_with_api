from django.urls import path
from .views import *
from .requests_to_api import *


urlpatterns = [
    path('', view_home_page, name='home_page_url'),
    path('search/', view_response, name='search_view_url'),
    path('search/<str:id>', game_detail_view, name='game_detail_url'),
    path('search/<str:deal_id>/', deal_detail_view, name='deal_detail_url')
]
