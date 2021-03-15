from .models import Games
from .views import *
from django.db.models import F
from django.shortcuts import render
from .requests_to_api import requester
from django.views.generic import View


class GameDetailMixin(View):
    def get(self, request, internalName, statistic):
        """ Функция, чтобы детально показать информацию по конкретной игре,
            через её internalName.
        """
        obj_title = requester.get_games(title=internalName)
        obj_id = requester.get_games(id=obj_title[0]['gameID'])  # Здесь осуществляется запрос по ID игры.
        deal_info = requester.get_deal(obj_title[0]['cheapestDealID'])  # Здесь делается
        # запрос по ID самого дешевого предложения.
        stores_info = requester.get_stores()  # Запрос, чтобы собрать инфу по магазинам.
        stores_dict = store_dictionary(stores_info)
        if statistic == '1':  # Если "1", происходит запись в БД
            statistic_record(obj_title[0]['external'], obj_title[0]['gameID'], internalName)
        return render(request, 'api_app/game_detail.html', context={
            'obj': obj_id, 'deal': deal_info, 'stores_dict': stores_dict,
            'stores_links': stores_links
        })


def store_dictionary(info):
    """ Чтобы по ID магазина вывести его storeName, сделал
        словарь типа: {'1': 'Steam', '2': Gamesplanet, '3': '...'}
    """
    return dict(zip([item['storeID'] for item in info], [item['storeName'] for item in info]))


def statistic_record(title, game_id, internalName):
    """ Функция, для записи названия игры в БД
        и подсчёта кол-ва просмотров
    """
    game, created = Games.objects.get_or_create(title=title, game_id=game_id, internalName=internalName)
    game.game_views = F('game_views') + 1
    game.save()


""" Эти ссылки отправляются в шаблон game_detail.html """
stores_links = {
    '1': 'https://store.steampowered.com/', '2': 'https://www.gamersgate.com/',
    '3': 'https://www.greenmangaming.com/', '4': 'https://www.amazon.com/', '5': 'http://www.gamestop.com/',
    '6': 'https://www.direct2drive.com/', '7': 'https://www.gog.com/', '8': 'https://www.origin.com/',
    '9': 'Get Games', '10': 'https://shinyloot.com/',
    '11': 'https://www.humblebundle.com/store', '12': 'https://www.desura.com/',
    '13': 'https://store.ubi.com/', '14': 'http://indiegamestand.com/', '15': 'https://www.fanatical.com/en/',
    '16': 'https://www.gamesrocket.com/', '17': 'https://gamesrepublic.com/',
    '18': 'https://store.silagames.com/', '19': 'http://playfield.io/',
    '20': 'https://www.imperialgames.co.uk/shop/index.php', '21': 'https://www.wingamestore.com/',
    '22': 'http://www.funstockdigital.co.uk/', '23': 'https://www.gamebillet.com/',
    '24': 'https://www.voidu.com/', '25': 'https://www.epicgames.com/store', '26': 'Razer Game Store',
    '27': 'https://uk.gamesplanet.com/',
    '28': 'https://www.gamesload.com/home.html', '29': 'https://2game.com/',
    '30': 'https://www.indiegala.com/', '31': 'https://eu.shop.battle.net/',
    '32': 'https://www.allyouplay.com/en/'
}
