import os
import sys
import json

from .ApiRequests import ApiRequests


class CommandTools:

    @staticmethod
    def execute_login():
        """ This method will try to login the user. If the user does no have an assigned token, they will log in with
        'login [username] [password]'. If they have MFA set up, the will receive a code through the specified medium.
        They will then have to run login again with 'login [username] [password] [MFA-code] to receive the token. If
        they don't have MFA, then they will be logged in a given a token. The token will be stored in a text file that
        should be updated when the user receives a new token. Do not commit the file generated

        :return: None (If we choose to we can return the API response)
        """
        username = sys.argv[2]
        password = sys.argv[3]

        # If the number of arguments is 5, the MFA token was passed in. Check if a new token needs to be written
        if len(sys.argv) == 5:
            mfa_code = sys.argv[4]
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

            # THIS WILL BE DELETED AFTER TEST
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

        print(response.text)

    @staticmethod
    def execute_logout():
        """ This method will try to log out the user. When the user logs out, their token will be invalidated. Upon login,
        they will receive a new token. If the user does not have a token text file, they cannot log out

        :return: None (If we choose to we can return the API response)
        """

        if os.path.exists('robinhood_token.txt'):
            response = ApiRequests.logout(CommandTools.get_token())

            print('There will be no response if logout is successful')
            print(response.text)

        else:
            print('You cant logout if you do not have an assigned token yet')
            sys.exit()

    @staticmethod
    def get_token():
        """ Simple helper that will return the token stored in the text file.

        :return: Your Robinhood API token
        """

        robinhood_token_file = open('robinhood_token.txt')
        current_token = robinhood_token_file.read()

        return current_token