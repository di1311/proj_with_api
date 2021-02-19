import requests


class RequestApi:
    """ Класс, который делает запрос, я хз"""
    url_games = 'https://www.cheapshark.com/api/1.0/games'

    def get_games(self, **kwargs):
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


requester = RequestApi()
