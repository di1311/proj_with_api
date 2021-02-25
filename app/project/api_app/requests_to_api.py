import requests


class RequestApi:
    """ Класс, который делает запрос, я хз"""
    url_games = 'https://www.cheapshark.com/api/1.0/games'
    url_stores = 'https://www.cheapshark.com/api/1.0/stores'
    url_deals = 'https://www.cheapshark.com/api/1.0/deals'

    def get_games(self, **kwargs):
        """ Запрос для получения списка игр
            и запрос для информации по конкретной игре
            (чтобы кликнуть на имя игры и сделать второй запрос по id).
        """
        params = dict(**kwargs)
        res_obj = requests.get(RequestApi.url_games, params=params)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            if res_obj_json:
                return res_obj_json
            else:
                return 'Nothing found'
        else:
            print('Shto-to ne tak')

    def get_stores(self):
        """ Запрос для получения списка магазинов,
            который я отправляю контекстом в шаблон,
            но пока не применяю эту инфу.
        """
        res_obj = requests.get(RequestApi.url_stores)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            if res_obj_json:
                return res_obj_json
            else:
                return 'Nothing found'

    def get_deal(self, deal_id):
        """ Запрос по конкретному предложению (по его id),
            отправляется когда на цену жмешь.
        """
        deal_obj = requests.get(RequestApi.url_deals + '?id=' + deal_id)
        if deal_obj.status_code == 200:
            deal_obj_json = deal_obj.json()
            if deal_obj_json:
                return deal_obj_json
            else:
                return 'Nothing found'

    def store_dictionary(self, info):
        """ Чтобы по ID магазина вывести его storeName, сделал
            словарь типа: {'1': 'Steam', '2': Gamesplanet, '3': '...'}
        """
        return dict(zip([item['storeID'] for item in info], [item['storeName'] for item in info]))


requester = RequestApi()
