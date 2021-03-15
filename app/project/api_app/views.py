from django.shortcuts import render
from .requests_to_api import requester
from .utils import GameDetailMixin
from django.views.generic import View
from .models import Games


class ViewHomePage(View):
    def get(self, request):
        """ Вьюха для домашней страницы """
        return render(request, 'base.html')


class GameDetailView(GameDetailMixin, View):
    def search_games(self, request):
        """ Эта функция отправляет результат post запроса
            (по title игры) в шаблон.
        """
        title = request.POST['search']
        obj_title = requester.get_games(title=title)
        return render(request, 'api_app/index.html', context={'obj': obj_title, 'title': title})


class PopularGamesView(GameDetailMixin, View):
    def popular_games_view(self, request):
        """ Функция, чтобы вывести список из трёх самых популярных игр. """
        games = Games.objects.order_by('-game_views')[:3]
        return render(request, 'api_app/popular_games.html', context={'games': games})
