from django.shortcuts import render
from .requests_to_api import requester
from .utils import statistic_record, store_dictionary
from django.views.generic import View
from .models import Games
from .config import stores_links


class ViewHomePage(View):
    def get(self, request):
        """ Вьюха для домашней страницы """
        return render(request, 'base.html')


class GameDetailView(View):
    def get(self, request, internal_name=None):
        """ Функция, чтобы детально показать информацию по конкретной игре,
            через её internalName.
        """
        if internal_name is None:  # если пользователь вводит 'localhost/search'.
            return render(request, 'api_app/please_use_searchForm.html')
        query = request.GET.get('statistic', None)
        obj_title = requester.get_games(title=internal_name)
        obj_id = requester.get_games(id=obj_title[0]['gameID'])  # Здесь осуществляется запрос по ID игры.
        deal_info = requester.get_deal(obj_title[0]['cheapestDealID'])  # Здесь делается
        # запрос по ID самого дешевого предложения.
        stores_info = requester.get_stores()  # Запрос, чтобы собрать инфу по магазинам.
        stores_dict = store_dictionary(stores_info)
        if query:  # Если передаётся query параметр, то происходит запись игры в БД.
            statistic_record(obj_title[0]['external'], obj_title[0]['gameID'], internal_name, obj_title[0]['thumb'])
        return render(request, 'api_app/game_detail.html', context={
            'obj': obj_id, 'deal': deal_info, 'stores_dict': stores_dict,
            'stores_links': stores_links
        })

    def post(self, request):
        """ Эта функция отправляет результат post запроса
                    (по title игры) в шаблон.
        """
        title = request.POST['search']
        obj_title = requester.get_games(title=title)
        return render(request, 'api_app/index.html', context={'obj': obj_title, 'title': title})


class PopularGamesView(View):
    def get(self, request):
        """ Функция, чтобы вывести список из трёх самых популярных игр. """
        games = Games.objects.order_by('-game_views')[:3]
        return render(request, 'api_app/popular_games.html', context={'games': games})
