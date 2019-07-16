from urllib.parse import urlencode
import requests

APP_ID = 7058177
AUTH_URL = 'https://oauth.vk.com/authorize'
Auth_DATA = {
    'client_id' : APP_ID,
    'display' : 'page',
    'scope' : 'status',
    'response_type' : 'token',
}
# print('?'.join((AUTH_URL, urlencode(Auth_DATA))))



TOKEN = '4c4851cbaeeb90b218be4aaf9dfbdd4fb43d673e7cbf48397127f43181a02fda2ed7dce5e014e9ab818da'
class User:
    def __init__(self,user_id, token):
        self.token = token
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token' : self.token,
            'v' : '5.25',
            'user_id' : self.user_id
        }

    def request(self, method, params):
        response = requests.get(
                'https://api.vk.com/method/' + method,
                params=params
            )
        return response


    def get_friends(self):
        params = self.get_params()
        response = self.request(
            'friends.get',
            params=params
        )
        return response.json()['response']

    def __and__(self, other_user, mutal_user_lust=list()):
        user_1 = other_user.get_friends()
        user_2= self.get_friends()
        for i in user_1.get('items'):
            # print(i)
            for ii in user_2.get('items'):
                if i == ii:
                    adress = 'https://vk.com/id' + str(ii)
                    mutal_user_lust.append(adress)
        return mutal_user_lust

    def user(self, id):
        response = requests.get(
            'https://vk.com/id' + id,
        )
        return response


Alina = User('61125176',TOKEN)
Ilya = User('306008470',TOKEN)
print(Alina & Ilya)