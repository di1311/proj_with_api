from .models import Games
from .views import *
from django.db.models import F
from django.shortcuts import render
from .requests_to_api import requester
from django.views.generic import View


def store_dictionary(info):
    """ Чтобы по ID магазина вывести его storeName, сделал
        словарь типа: {'1': 'Steam', '2': Gamesplanet, '3': '...'}
    """
    return dict(zip([item.get('storeID', None) for item in info], [item.get('storeName', None) for item in info]))


def statistic_record(title, game_id, internalName, thumb):
    """ Функция, для записи названия игры в БД
        и подсчёта кол-ва просмотров
    """
    game, created = Games.objects.get_or_create(title=title, game_id=game_id, internalName=internalName, image_link=thumb)
    game.game_views = F('game_views') + 1
    game.save()



