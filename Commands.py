import sys

from AutomatedTrading.ProgramCommands import ProgramCommands

if __name__ == '__main__':

    # If the user didn't specify a command. Break immediately
    if len(sys.argv) == 1:
        print('You must specify a command EX: login [username] [password]')
        sys.exit()

    command_name = sys.argv[1].casefold()
    argument_count = len(sys.argv) - 1

    if command_name == 'login':
        if argument_count == 3:
            ProgramCommands.login(sys.argv[2], sys.argv[3])
        elif argument_count == 4:
            ProgramCommands.login(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print('The login command does not accept these parameters')

    elif command_name == 'logout':
        ProgramCommands.logout()

    elif command_name == 'data':
        ProgramCommands.get_fundamental_data()

    else:
        print('Command does no exist or number of parameters for command was incorrect')
