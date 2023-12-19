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

import re
import random
import stdiomask

users = {}


# -----CLASSES-----

# -----FUNCTIONS-----

# Welcome message
def welcome():
    print("\nWelcome to FatWest Bank")


# Main menu
def main_menu():
    user_input = input("""Please select from one of the following options:
              1 - Login
              2 - Register
              : """)
    while user_input not in ['1', '2']:
        print("Input is not valid\n")
        selection = input("""Please select from one of the following options:
              1 - Login
              2 - Register
              : """)


# Register new user
def register_new_user():
    forename = input("Please enter your forename: ")
    surname = input("Please enter your surname: ")
    name_validation = input(
        f"Your name is {forename} {surname}, is this correct? Yes/No: ")
    while name_validation.lower() != 'yes':
        print("Please try again")
        forename = input("Please enter your forename: ")
        surname = input("Please enter your surname: ")
        name_validation = input(
            f"Your name is {forename} {surname}, is this correct? Yes/No: ")
    
    id_num = id_num_generator()
    user_id = f"{forename[0].lower()}{surname[:5].lower()}{id_num}"
    print(f"Your user id is {user_id}\n")
    
    password = stdiomask.getpass("""Please create a password.
Passwords must be alphanumerical,
must contain at least one uppercase letter,
must contain at least one lowercase letter,
must contain at least 8 characters.
Create a password now:  """, mask="*")
    while True:
        password2 = stdiomask.getpass("Please re-enter your password: ")
        if (len(password) >= 8 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        password == password2):
            break
        else:
            password = stdiomask.getpass("""\nInvalid password, please try again.
Passwords must match and be alphanumerical,
must contain at least one uppercase letter,
must contain at least one lowercase letter,
must contain at least 8 characters.
Create a password now: """, mask="*")
    
    print(f"\nCongratulations {forename}, your account has been created successfully.")
            
        
# User id number generator
def id_num_generator():
    return random.randint(1000, 9999)


# -----MAIN PROGRAM-----

while True:
    welcome()
    # main_menu()
    register_new_user()
    print("Thanks!")
    exit()
