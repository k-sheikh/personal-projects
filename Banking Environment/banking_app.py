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

    def apply_interest(self, amount):
        self.balance += (self.balance * self.interest_rate)
        return self.balance
