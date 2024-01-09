class User:
    def __init__(self, forename, surname, user_id, password):
        self.forename = forename
        self.surname = surname
        self.user_id = user_id
        self.password = password
        self.account = {}

    def add_account(self, account):
        self.account[account.account_number] = account