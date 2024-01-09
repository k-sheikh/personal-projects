from user import User
from account import Account
from utilities import generate_user_id, generate_account_number

class Bank:
    def __init__(self):
        self.users = {}

    def register_user(self, forename, surname, password):
        user_id = generate_user_id(forename, surname)
        new_user = User(forename, surname, user_id, password)
        self.users[user_id] = new_user
        return new_user
    
    def create_account(self, user_id, account_type):
        account_number = generate_account_number()
        account = Account(account_number, account_type)
        self.users[user_id].add_account(account)
        return account