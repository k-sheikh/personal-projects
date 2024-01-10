from user import User
from account import Account
from utilities import generate_user_id, generate_account_number

class Bank:
    def __init__(self):
        self.users = {}

    def register_user(self, forename, surname, password):
        try:
            user_id = generate_user_id(forename, surname)
            if user_id in self.users:
                raise ValueError("User already exists")
            new_user = User(forename, surname, user_id, password)
            self.users[user_id] = new_user
            return new_user
        except Exception as e:
            print(f"Error in user registration: {e}")
    
    def create_account(self, user_id, account_type):
        try:
            if user_id not in self.users:
                raise ValueError("User does not exist")
            account_number = generate_account_number()
            account = Account(account_number, account_type)
            self.users[user_id].add_account(account)
            return account
        except Exception as e:
            raise Exception(f"Error in account creation: {e}")