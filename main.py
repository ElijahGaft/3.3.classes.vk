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
    def __init__(self, token):
        self.token = token

    def get_params(self):
        return {
            'access_token' : self.token,
            'v' : '5.25'
        }

    def request(self, method, params):
        response = requests.get(
                'https://api.vk.com/method/' + method,
                params=params
            )
        return response


    def get_status(self):
        params = self.get_params()
        response = self.request(
            'status.get',
            params=params
        )
        return response.json()['response']['text']

    def set_status(self, text):
        params = self.get_params()
        params['text'] = text
        response = self.request(
            'status.set',
            params=params
        )
        return response.json()['response']

Ilya = User(TOKEN)
Ilya.set_status('твои мысли становятся твоей жизнью')
status = Ilya.get_status()
print(status)
