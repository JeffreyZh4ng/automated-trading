import os
import sys
import json
from AutomatedTrading.Login import Login


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('You must specify a command EX: Login, Logout...')
        sys.exit()

    command_name = sys.argv[1]
    command_name = command_name.casefold()

    if command_name == 'login':
        username = sys.argv[2]
        password = sys.argv[3]

        response = ''
        if len(sys.argv) == 5:
            mfa_code = sys.argv[4]
            print('Entering the MFA %s' % mfa_code)
            response = Login.login_with_mfa(username, password, mfa_code)

        else:
            print('Entering login credentials')
            response = Login.login_with_credentials(username, password)

        if response.status_code == 200:
            json_data = json.loads(response.text)
            token = json_data['token']
            os.environ["ROBINHOOD_CURRENT_LOGIN_TOKEN"] = token

        print(response.text)
        sys.exit()