# -----LIBRARIES-----

import random

users = {}
# users = {user_id: {forename: 'John', surname: 'Smith', password: 'abc123',
#                    accounts: {acc_num: {acc_type: "Current Account", balance: 1000}}}}


# -----CLASSES-----

# Parent class
class Bank:
    def __init__(self, user_id, password, forename, surname, acc_num):
        self.user_id = user_id
        self.password = password
        self.forename = forename
        self.surname = surname
        self.balance = 0
        self.acc_num = acc_num

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

    @staticmethod
    def acc_num_generator():
        return random.randint(10000000, 99999999)

    @staticmethod
    def validate_password(password):
        # Ensure password is >= 8 chars and contains a number
        return len(password) >= 8 and any(char.isdigit() for char in password)


# Child class
class CurrentAccount(Bank):
    def __init__(self, user_id, password, forename, surname, acc_num):
        super().__init__(user_id, password, forename, surname, acc_num)
        self.acc_type = "Current Account"
        self.overdraft_limit = 1000

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Insufficient funds. Overdraft limit reached"
        else:
            self.balance -= amount
            return self.balance


class SavingsAccount(Bank):
    def __init__(self, user_id, password, forename, surname, acc_num):
        super().__init__(user_id, password, forename, surname, acc_num)
        self.acc_type = "Savings Account"
        self.interest_rate = 0.05

    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate)
        return self.balance


# -----FUNCTIONS-----

# Account number generator
# def acc_num_generator():
#     return random.randint(100000, 999999)


# Create new password
def validate_new_password():
    password = input("Create a password: ")
    while not Bank.validate_password(password):
        print("""\nPasswords must be alphanumerical and at least 8 characters with upper and lowercase letters
Please try again\n""")
        password = input("Create a password: ")
    return password


# Register new user
def registration():
    forename = input("\nEnter your forename: ")
    surname = input("Enter your surname: ")
    user_id = input("Create a user id: ")

    password = validate_new_password()
    password2 = input("Re-enter your password: ")
    while not password2 == password:
        print("\nThe passwords do not match, please try again\n")
        password = validate_new_password()
        password2 = input("Re-enter your password: ")

    acc_num = Bank.acc_num_generator()

    print("Account created successfully")
    print(f"""Account details:
Forename:\t{forename}
Surname:\t{surname}
User ID:\t{user_id}
Acc No:\t\t{acc_num}
Acc Type:\tPLACEHOLDER""")


# Login
def login():
    user_id = input("Enter user_id: ")
    password = input("Enter password: ")


def main_menu():
    main_menu_option = input("""\nPlease select from one of the following options:
1 -\tLogin
2 -\tCreate new account
0 -\tExit
Enter:  """)

    if main_menu_option == "1":
        login()
    elif main_menu_option == "2":
        registration()
    elif main_menu_option == "0":
        exit()
    else:
        print("Invalid input, please try again\n")


# -----MAIN PROGRAM-----

print("\nWelcome to FatWest Bank")

while True:
    main_menu()
