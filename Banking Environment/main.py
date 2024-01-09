# BANKING ENVIRONMENT

# -----PSEUDOCODE-----

"""
# Program Structure Overview

Main Menu
	Welcome, Login, Register, Exit
		Login
			Enter user id, Enter password
				You have no accounts, Create account
					Account type: Savings, Current
					Save Classes to txt
				Select account
					Check balance, Withdraw, Deposit
						Deposit with cash, transfer from another account
				Create new account
					Account type: Savings, Current
					Save Classes to txt
		Register
			Create user id, password
			Verify user id, password
			Check for match, save to txt
"""

"""
# Dictionary Structure

users = {user_id : {
                    'forename' : 'John',
                    'surname' : 'Smith',
                    'password' : 'password123'
                    'accounts' : {
                                'account_num' : 12345678
                                'account_type' : 'Current Account'
                                'balance' : 5000
                    }}}
"""


# -----LIBRARIES-----

from bank import Bank
from sys import exit
import re
import stdiomask

users = {}


# -----FUNCTIONS-----

# Welcome message
def welcome():
    print("\nWelcome to FatWest Bank")


# Main menu
def main_menu(bank):
    user_input = input("""Please select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """)
    while user_input not in ['1', '2', '3']:
        print("\nInput is not valid.")
        user_input = input("""Please select from one of the following options:
1 - Login
2 - Register
3 - Exit
: """)
    if user_input == '1':
        pass
    elif user_input == '2':
        register_new_user(bank)
    elif user_input == '3':
        print("\nThankyou for banking with FatWest. Goodbye!")
        exit()


# Register new user
def register_new_user(bank):
    forename = input("\nPlease enter your forename: ")
    surname = input("Please enter your surname: ")
    name_validation = input(
        f"Your name is {forename} {surname}, is this correct? Yes/No: ")
    while name_validation.lower() != 'yes':
        print("\nPlease try again")
        forename = input("Please enter your forename: ")
        surname = input("Please enter your surname: ")
        name_validation = input(
            f"\nYour name is {forename} {surname}, is this correct? Yes/No: ")
        
    # Password and validation
    print("\nPlease create a password.")
    while True:
        password = stdiomask.getpass("""Passwords must be alphanumerical,
must contain at least one uppercase letter,
must contain at least one lowercase letter,
must contain at least 8 characters.
Create a password now:  """, mask="*")
        
        # Check password criteria
        if (len(password) >= 8 and
            re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password)):
            
            # Re-enter the password
            password2 = stdiomask.getpass("Please re-enter your password: ")
            
            # Check if passwords match
            if password == password2:
                break
            else:
                print("\nPasswords do not match. Please start again.")
        else:
            print("\nInvalid password, please try again.")

    new_user = bank.register_user(forename, surname, password)
    user_id = new_user.user_id

    print(f"""\nCongratulations {forename}, your account has been created successfully.
Your user id is {user_id}. Please keep this information safe.""")


# -----MAIN PROGRAM-----

if __name__ == "__main__":
    fatWestBank = Bank()
    while True:
        welcome()
        main_menu(fatWestBank)