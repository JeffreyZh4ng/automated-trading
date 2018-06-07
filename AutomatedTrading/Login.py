import requests


class Login:

    @staticmethod
    def login_with_credentials(username, password):
        headers = {
            'Accept': 'application/json',
        }

        data = [
            ('username', username),
            ('password', password),
        ]

        response = requests.post('https://api.robinhood.com/api-token-auth/', headers=headers, data=data)
        return response

    @staticmethod
    def login_with_mfa(username, password, mfa_code):
        headers = {
            'Accept': 'application/json',
        }

        data = [
            ('username', username),
            ('password', password),
            ('mfa_code', mfa_code),
        ]

        response = requests.post('https://api.robinhood.com/api-token-auth/', headers=headers, data=data)
        return response
