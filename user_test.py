import unittest  # Importing the unittest module
from user import User  # Importing the User class
from user import Credentials


class TestUser(unittest.TestCase):

    '''
       Test class that defines test cases for the user class behaviours.
       Args:
          unittest.TestCase: TestCase class that helps in creating test cases
       '''

    def setUp(self):
        '''

        Set up method to run before each test cases.
        '''
        self.new_user = User("Mary", "Mario123")  # create user object

    def test_init(self):
        '''
          test_init test case to test if the object is initialized properly
          '''
        self.assertEqual(self.new_user.username, "Mary")
        self.assertEqual(self.new_user.password, "Mario123")

    def test_save_user(self):
        '''
             test_save_user test case to test if the user object is saved into
              the user list
             '''
        self.new_user.save_user()  # saving the new user details
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):
    '''
      Test class that defines test cases for credentials.
    '''

    def setUp(self):
        '''
            setUp method to run before each test case.
          '''
        self.new_credentials = Credentials("Gmail", "Ivy_kabere", "Kabere@254")

    def test_init(self):
        '''
        test_init test case to test if the object is initailized correctly
        '''
        self.assertEqual(self.new_credentials.account, "Gmail")
        self.assertEqual(self.new_credentials.username, "Ivy_kabere")
        self.assertEqual(self.new_credentials.password, "Kabere@254")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the the credentials object is saved into the credentials_list
        '''
        self.new_credentials.save_credentials()  # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials test case to test if the credentials saves multiple objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "Martha21", "Xrtm345")
        # new Credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove credentials detail from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "Martha21", "Xrtm345")
        # new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        # deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
