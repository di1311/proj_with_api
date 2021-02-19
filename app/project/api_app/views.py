from django.shortcuts import render
from .requests_to_api import requester
from django.views.generic import View


def view_home_page(request):
    """
        Вьюха для домашней страницы
    """
    return render(request, 'base.html')


def view_response(request):
    """ Эта функция обрабатывает результат get запроса,
        возвращает три интересующих поля по каждой игре: gameID (чтобы сделать запрос по конкретной игре, нужен id),
        название игры и самую низкую цену.
    """
    title = request.POST
    obj = requester.get_games(title)
    return render(request, 'api_app/index.html', context={'obj': obj})


def game_detail_view(request, game_id):
    """ Функция, чтобы детально показать информацию по конкретной игре,
        через её ID.
    """
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAA', game_id)
    pass
