import sys
from AutomatedTrading.Login import TestClass


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    response = TestClass.login(username,password)
    print(response.text)