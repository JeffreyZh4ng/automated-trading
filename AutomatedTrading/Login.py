import json
import requests


class TestClass:

    @staticmethod
    def login(username, password):
        headers = {
            'Accept': 'application/json',
        }

        data = [
            ('username', username),
            ('password', password),
        ]

        response = requests.post('https://api.robinhood.com/api-token-auth/', headers=headers, data=data)
        return response
