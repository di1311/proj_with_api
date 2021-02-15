from django.shortcuts import render
from .requests_to_api import requester
from django.views.generic import View


def view_response(request):
    """ Эта функция обрабатывает результат get запроса,
        возвращает три интересующих поля по каждой игре: gameID (чтобы сделать запрос по конкретной игре, нужен id),
        название игры и самую низкую цену.
    """
    obj = requester.get_games()
    return render(request, 'api_app/base.html', context={'obj': obj})
