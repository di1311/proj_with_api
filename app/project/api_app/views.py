from django.shortcuts import render
from .requests_to_api import RequestApi
from django.views.generic import View


def view_response(request):
    """ Эта функция обрабатывает результат get запроса,
        возвращает три интересующих поля по каждой игре: gameID (чтобы сделать запрос по конкретной игре, нужен id),
        название игры и самую низкую цену.
    """
    list_of_games = []
    obj = RequestApi.get()
    for index in range(len(obj)):
        games_info = obj[index]['gameID'], obj[index]['external'], obj[index]['cheapest']
        list_of_games.append(games_info)
    return render(request, 'index.html', context={'obj': list_of_games})

