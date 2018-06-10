import os
import io
import sys
import json

from AutomatedTrading.Login import Login


if __name__ == '__main__':

    # If the user didn't specify a command. Break immediately
    if len(sys.argv) < 2:
        print('You must specify a command EX: login [username] [password]')
        sys.exit()

    argument_count = len(sys.argv)
    command_name = sys.argv[1]
    command_name = command_name.casefold()

    if command_name == 'login' and (argument_count == 4 or argument_count == 5):
        username = sys.argv[2]
        password = sys.argv[3]

        # If the number of arguments is 5, the MFA token was passed in. Check if a new token needs to be written
        if len(sys.argv) == 5:
            mfa_code = sys.argv[4]
            response = Login.login_with_mfa(username, password, mfa_code)

            if response.status_code == 200:
                json_data = json.loads(response.text)
                response_token = json_data['token']

                if os.path.exists('robinhood_token.txt'):
                    robinhood_token_file = open('robinhood_token.txt')
                    current_token = robinhood_token_file.read()
                    if response_token != current_token:
                        robinhood_token_file.truncate()
                        robinhood_token_file.write(response_token)
                        robinhood_token_file.close()

                else:
                    robinhood_token_file = open('robinhood_token.txt', 'w+')
                    robinhood_token_file.write(response_token)
                    robinhood_token_file.close()

        # If the number of arguments is 4, the user is requesting a MFA code from SMS or MFA has not been setup
        else:
            print('Entering login credentials')
            response = Login.login_with_credentials(username, password)

        print(response.text)
        sys.exit()

    elif command_name == 'logout':
        response = Login.logout()
        print(response.text)

    else:
        print('Command does no exist or number of parameters for command was incorrect')