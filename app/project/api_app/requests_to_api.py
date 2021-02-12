import requests
""" Чтобы обращаться к разным функциям api, 
    но пока это бесполезно
"""
sequel = input('if you need list of games, input "games"  ')
url = 'https://www.cheapshark.com/api/1.0/' + sequel


class RequestApi:
    """ Класс, который делает запрос, я хз"""

    @staticmethod
    def get():
        global url
        params = payload_func(payload)
        res_obj = requests.get(url, params=params)
        if res_obj.status_code == 200:
            res_obj_json = res_obj.json()
            return res_obj_json
        else:
            print('Shto-to ne tak')


payload = input('Введите название игры ')


def payload_func(payload):
    return {'title': payload}
