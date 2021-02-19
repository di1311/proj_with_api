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
    # stores_info = requester.get_stores()
    obj = requester.get_games(id=id)
    return render(request, 'api_app/game_detail.html', context={'obj': obj})


def deal_detail_view(request, deal_id):
    """ Функция для детального deal """
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', deal_id, type(deal_id))
    deal_info = requester.get_deal(deal_id)
    stores_info = requester.get_stores()
    return render(request, 'api_app/deal_detail.html', context={'deal': deal_info, 'stores': stores_info})
