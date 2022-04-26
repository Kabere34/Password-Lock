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


def create_new_credentials(account, userName, password):
    """
        Function that creates new credentials for a given user account
    """
    new_credentials = Credentials(account, userName, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save Credentials to the credentials list
    '''
    return credentials.save_credentials()


def display_credentials():
    '''
    Function to display credentials
    '''
    return Credentials.display_credentials()


def del_credentials(credentials):
    '''
    Function to delete Credentials in the credentials list
    '''
    credentials.delete_credentials()


def find_credentials(account):
    '''
    Function that finds a credentials by account and returns the credential
    '''

    return Credentials.find_by_account(account)


def check_existing_credentials(account):
    '''
    Function that checks if credentials exists with that account and return a Boolean
    '''
    return Credentials.contact_exist(account)


def generate_password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatepassword()
    return auto_password


def main():

    print("Hello, Welcome to your password lock generator.Please enter one of the choices to proceed.\n CA - create a new account, DC - display account, LI-Have an account \n ")

    short_code = input().lower().split
    if short_code == 'CA':
        print("sign up")
        print('*' * 50)
        user_name = input("User_name: ")
        while True:
            print(
                " TP - To type your own pasword: \n GP-to generate random password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Your Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username, password))
        print("*"*85)
        print(
            f"Hello {user_name}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(
                    " TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credentials(
                account, userName, password))
            print('\n')
            print(
                f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print("Here's your list of accounts: ")

                print('*' * 30)
                print('_' * 30)
                for account in display_credentials():
                    print(
                        f" Account:{account.account} \n UserName:{userName}\n Password:{password}")
                    print('_' * 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(
                    f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(
                    f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print(
                    "That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(
                f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print(
                "Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':
    main()
