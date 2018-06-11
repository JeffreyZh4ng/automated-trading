import requests


class ApiRequests:

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

    @staticmethod
    def logout(token):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Token %s' % token,
        }

        response = requests.post('https://api.robinhood.com/api-token-logout/', headers=headers)
        return response

    @staticmethod
    def get_data(ticker_symbol):
        headers = {
            'Accept': 'application/json'
        }

        response = requests.get('https:://api.robinhood.com/fundamentals/' + ticker_symbol + '/', headers=headers)
        return response
