from django.shortcuts import render
from .requests_to_api import requester
from django.views.generic import View


def view_home_page(request):
    """ Вьюха для домашней страницы """
    return render(request, 'base.html')


def view_response(request):
    """ Эта функция обрабатывает результат get запроса,
        возвращает три интересующих поля по каждой игре: gameID (чтобы сделать запрос по конкретной игре, нужен id),
        название игры и самую низкую цену.
    """
    title = request.POST['search']
    obj = requester.get_games(title=title)
    return render(request, 'api_app/index.html', context={'obj': obj})


def game_detail_view(request, id):
    """ Функция, чтобы детально показать информацию по конкретной игре,
        через её ID.
    """
    """ Чтобы по ID магазина вывести его storeName, сделал 
        словарь типа: {'1': 'Steam', '2': Gamesplanet, '3': '....'}
    """
    obj = requester.get_games(id=id)
    stores_info = requester.get_stores()
    shop_dict = dict(zip([item['storeID'] for item in stores_info], [item['storeName'] for item in stores_info]))
    return render(request, 'api_app/game_detail.html', context={'obj': obj, 'shop_dict': shop_dict})


def deal_detail_view(request, deal_id):
    """ Функция для детального deal """
    deal_info = requester.get_deal(deal_id)
    stores_info = requester.get_stores()
    return render(request, 'api_app/deal_detail.html', context={'deal': deal_info, 'stores': stores_info})
