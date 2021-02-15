import requests


class RequestApi:
    """ Класс, который делает запрос, я хз"""
    payload = input('Введите название игры ')
    url = 'https://www.cheapshark.com/api/1.0/games'

    def get_games(self):
        params = requester.payload_func(RequestApi.payload)
        res_obj = requests.get(RequestApi.url, params=params)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            return res_obj_json
        else:
            print('Shto-to ne tak')

    def payload_func(self, payload):
        return {'title': payload}


requester = RequestApi()
