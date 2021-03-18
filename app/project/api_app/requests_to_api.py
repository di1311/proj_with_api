import requests


# noinspection PyMethodMayBeStatic
class RequestApi:
    """ Класс, который делает запрос, я хз """
    url_games = 'https://www.cheapshark.com/api/1.0/games'
    url_stores = 'https://www.cheapshark.com/api/1.0/stores'
    url_deals = 'https://www.cheapshark.com/api/1.0/deals'

    def get_games(self, **kwargs):
        """ Запрос для получения списка игр
            и запрос для информации по конкретной игре
            (чтобы кликнуть на имя игры и сделать второй запрос по id).
        """
        res_obj = requests.get(self.url_games, params=kwargs)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            if res_obj_json:
                return res_obj_json
            else:
                return 'Nothing found'

    def get_stores(self):
        """ Запрос для получения списка магазинов,
            который я отправляю контекстом в шаблон.
        """
        res_obj = requests.get(self.url_stores)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            if res_obj_json:
                return res_obj_json
            else:
                return 'Nothing found'

    def get_deal(self, deal_id):
        """ Запрос по конкретному предложению (по его deal_id),
            отправляется когда на цену жмешь.
        """
        deal_obj = requests.get(self.url_deals + '?id=' + str(deal_id))
        if deal_obj.status_code == 200:
            deal_obj_json = deal_obj.json()
            if deal_obj_json:
                return deal_obj_json
            else:
                return 'Nothing found'


requester = RequestApi()
