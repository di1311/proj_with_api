from django.shortcuts import render
from .requests_to_api import requester
from .utils import stores_links


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


def game_detail_view(request, id, deal_id):
    """ Функция, чтобы детально показать информацию по конкретной игре,
        через её id, и deal_id.
    """
    obj = requester.get_games(id=id)
    deal_info = requester.get_deal(deal_id)
    stores_info = requester.get_stores()
    stores_dict = requester.store_dictionary(stores_info)
    print(stores_dict)
    return render(request, 'api_app/game_detail.html', context={
        'obj': obj, 'deal': deal_info, 'stores_dict': stores_dict,
        'stores_links': stores_links
    }
                  )
