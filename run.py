#!/usr/bin/env python3.10.4
from user import User, Credentials


def create_new_user(username, password):
    '''
    Function to create a new user
    '''

    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
      Function to save user
    '''
    user.save_user()


def display_user():
    '''
    Function to display existing user
    '''

    return User.display_user()


def login_user(username, password):
    """
        function that checks whether a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credentials(account, username, password):
    """
        Function that creates new credentials for a given user account
    """
    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save Credentials to the credentials list
    '''
    credentials.save_credentials()


def de_credentials(credentials):
    '''
    Function to delete Credentials in the credentials list
    '''
    credentials.delete_credentials()
