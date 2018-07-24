import os
import sys
import json

from .ApiRequests import ApiRequests


class ProgramCommands:

    @staticmethod
    def login(username, password, mfa_code=0):
        """ This method will try to login the user. If the user does no have an assigned token, they will log in with
        'login [username] [password]'. If they have MFA set up, they will receive a code most likely through SMS.
        They will then have to run login again with 'login [username] [password] [MFA-code] to receive the token. If
        they don't have MFA, then they will be logged in a given a token. The token will be stored in a text file that
        should be updated when the user receives a new token. Do not commit the file generated

        :param username: The users Robinhood username
        :param password: The users Robinhood password
        :param mfa_code: The mfa_code
        """

        # If the number of arguments is 5, the MFA token was passed in. Check if a new token needs to be written
        if mfa_code != 0:
            response = ApiRequests.login_with_mfa(username, password, mfa_code)

            if response.status_code == 200:
                json_data = json.loads(response.text)
                response_token = json_data['token']

                if os.path.exists('robinhood_token.txt'):
                    robinhood_token_file = open('robinhood_token.txt', 'r+')
                    current_token = robinhood_token_file.read()
                    if response_token != current_token:
                        robinhood_token_file.truncate()
                        robinhood_token_file.write(response_token)
                        robinhood_token_file.close()

                else:
                    robinhood_token_file = open('robinhood_token.txt', 'w+')
                    robinhood_token_file.write(response_token)
                    robinhood_token_file.close()
            else:
                print('Bad HTTP response: %s' % response.status_code)
                sys.exit()

        # If the number of arguments is 4, the user is requesting a MFA code from SMS or MFA has not been setup
        else:
            print('Entering login credentials')
            response = ApiRequests.login_with_credentials(username, password)

        print(response.text)

    @staticmethod
    def logout():
        """ This method will try to log out the user. When the user logs out, their token will be invalidated. Upon login,
        they will receive a new token. If the user does not have a token text file, they cannot log out

        :return: None (If we choose to we can return the API response)
        """

        if os.path.exists('robinhood_token.txt'):
            response = ApiRequests.logout()

            print('There will be no response if logout is successful')
            print(response.text)

        else:
            print('You cant logout if you do not have an assigned token yet')
            sys.exit()

    @staticmethod
    def get_fundamental_data():
        """ This method will try to collect the fundamental data -- price, PE ratio, daily high, daily low,
        annual high, annual low, etc.. -- for the requested security. The results, which will be returned in
        JSON format, will be stored in a text file. Do not commit the file.

        :return: None (If we choose to we can return the API response)
        """

        ticker_symbol = sys.argv[2]
        response = ApiRequests.get_data(ticker_symbol)

        if response.status_code == 200:
            if os.path.exists('ticker_data.txt'):
                ticker_data_file = open('ticker_data.txt', 'r+')
            else:
                ticker_data_file = open('ticker_data.txt', 'w+')

            ticker_data_file.write(response.text)
            ticker_data_file.close()

        else:
            print('Bad HTTP response: %s' % response.status_code)
            sys.exit()

