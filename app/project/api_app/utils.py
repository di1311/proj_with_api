from .models import Games
from .views import *
from django.shortcuts import render
from .requests_to_api import requester


def store_dictionary(self, info):
    """ Чтобы по ID магазина вывести его storeName, сделал
        словарь типа: {'1': 'Steam', '2': Gamesplanet, '3': '...'}
    """
    return dict(zip([item['storeID'] for item in info], [item['storeName'] for item in info]))


def statistic_record(title):
    """ Функция, для записи названия игры в БД
        и подсчёта кол-ва просмотров
    """
    Games.objects.get_or_create(title=title)
    # Games.objects.update_or_create(title=title)
    print(Games.objects.all())


def pull_need_query(obj, id):
    """ Фукнция, которая возвращает json ответ,
        с определенным ID конкретной игры.
    obj =
            [
       1) {'gameID': '610', 'steamAppID': '45700', 'cheapest': '15.99',
        'external': 'Devil May Cry 4'},
       2) {'gameID': '143864', 'steamAppID': '329050', 'cheapest': '8.79',
        'external': 'Devil May Cry 4 Special Edition'},
       3) {'gameID': '217384', 'steamAppID': None, 'cheapest': '3.99',
        'external': 'Devil May Cry 4 Special Edition - Lady and Trish Costumes'}
            ]
    Если id = 610, то вернёт 1 элемент json ответа.
    """
    for item in obj:
        if id in item.values():
            query = item
            return query


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
