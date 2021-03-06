import random
import string


class User:

    """Class that generates new instances of user details
    """

    user_list = []  # empty user list

    def __init__(self, username, password):
        '''
          __init__ method that helps us define properties for our objects.
        '''
        self.username = username

        self.password = password

    def save_user(self):
        '''
          save_user method saves user objects into user_list
          '''
        User.user_list.append(self)


class Credentials():
    """Class that generates new instances of credentials details
      """
    credentials_list = []  # Empty credentials list

    def __init__(self, account, username, password):
        """
         method that defines user credentials to be stored
         """
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''save_credentials method saves credentials object into contact_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
         delete_credentials method deletes a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        """
          Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def credentials_exist(cls, account):
        '''Method that checks if an account exists from the credentials list
        Args:
              account: account name to search if it exists
          Returns :
              Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account == account:

                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
         method that returns the credentials list
         '''
        return cls.credentials_list

    def generatepassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
