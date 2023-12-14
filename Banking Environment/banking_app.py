# BANKING ENVIRONMENT

# -----PSEUDOCODE-----

# Main Menu
# 	Welcome, Login, Register, Exit
# 		Login
# 			Enter user id, Enter password
# 				You have no accounts, Create account
# 					Account type: Savings, Current
# 					Save Classes to txt
# 				Select account
# 					Check balance, Withdraw, Deposit
# 						Deposit with cash, transfer from another account
# 				Create new account
# 					Account type: Savings, Current
# 					Save Classes to txt
# 		Register
# 			Create user id, password
# 			Verify user id, password
# 			Check for match, save to txt

# -----LIBRARIES-----

# -----CLASSES-----

# -----FUNCTIONS-----

def welcome():
    print("Welcome to FatWest Bank")


def main_menu():
    selection = input("""Please select from one of the following options:
              1 - Login
              2 - Register
              : """)
    while selection not in ['1', '2']:
        print("Input is not valid")
        selection = input("""Please select from one of the following options:
              1 - Login
              2 - Register
              : """)

# -----MAIN PROGRAM-----


while True:
    welcome()
    main_menu()
    print("Thanks!")
    exit()
