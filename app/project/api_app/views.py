from .utils import *
from django.views.generic import View


class ViewHomePage(View):
    def get(self, request):
        """ Вьюха для домашней страницы """
        return render(request, 'base.html')


class ViewResponse(View):
    def post(self, request):
        """ Эта функция отправляет результат post запроса
            (по title игры) в шаблон.
        """
        title = request.POST['search']
        obj = requester.get_games(title=title)
        if obj == 'Nothing found':
            return render(request, 'api_app/nothing_found.html')
        saver(obj)
        return render(request, 'api_app/index.html', context={'obj': obj})


def saver(obj):
    """ Нужно сохранить json ответ (obj = requester.get_games(title=title))
        чтобы отправить его в функцию pull_need_query.
        Сделал пока через try ... except, чтобы список не заполнялся
     """
    try:
        del list_with_obj[0]
    except IndexError:
        print('First element')
    return list_with_obj.append(obj)


list_with_obj = []


class GameDetailView(View):
    def get(self, request, id):
        """ Функция, чтобы детально показать информацию по конкретной игре,
            через её ID.
        """
        statistic_record(pull_need_query(list_with_obj[0], id)['external'])  # static_record('Devil May Cry 4') - пример
        obj = requester.get_games(id=id)
        deal_info = requester.get_deal(pull_need_query(list_with_obj[0], id)['cheapestDealID'])  # Здесь делается
        # запрос по ID самого дешевого предложения
        stores_info = requester.get_stores()
        stores_dict = requester.store_dictionary(stores_info)
        return render(request, 'api_app/game_detail.html', context={
            'obj': obj, 'deal': deal_info, 'stores_dict': stores_dict,
            'stores_links': stores_links
        }
                      )
