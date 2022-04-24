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

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove credentials detail from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "Martha21", "Xrtm345")
        # new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)
