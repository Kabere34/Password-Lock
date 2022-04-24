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
