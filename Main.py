import sys

from AutomatedTrading.ApiCommands import ApiCommands

if __name__ == '__main__':

    # I subtract one from the length of args because args includes Main.py
    argument_count = len(sys.argv) - 1
    command_name = sys.argv[1].casefold()

    # If the user didn't specify a command. Break immediately
    if argument_count == 0:
        print('You must specify a command EX: login [username] [password]')
        sys.exit()

    elif command_name == 'login' and (argument_count == 3 or argument_count == 4):
        ApiCommands.execute_login()

    elif command_name == 'logout':
        ApiCommands.execute_logout()

    elif command_name == 'data':
        ApiCommands.get_fundamental_data()

    else:
        print('Command does no exist or number of parameters for command was incorrect')
