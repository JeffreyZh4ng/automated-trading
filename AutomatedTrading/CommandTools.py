class CommandTools:

    @staticmethod
    def get_token():
        """ Simple helper that will return the token stored in the text file.

        :return: Your Robinhood API token
        """

        robinhood_token_file = open('robinhood_token.txt')
        current_token = robinhood_token_file.read()

        return current_token