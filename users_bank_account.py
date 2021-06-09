class BankAccount:
    
    accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest-rate: {self.int_rate}")
        return self
    
    def yield_interest(self):
        if self.balance <= 0:
            print(f"There are insufficient funds. You cannot gain interest.")
        else:
            self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    bank_name = "Bank of America"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}") 
        self.account.display_account_info()
        return self

    def transfer_money(self, amount, destination):
        self.account.withdraw(amount)
        destination.account.deposit(amount)
        self.display_user_balance()
        destination.display_user_balance()
        return self

david = User("David Bernard", "dpbernard18@gmail.com")
steph = User("Steph Rodriguez", "fakeemail@gmail.com")

david.make_deposit(1000)
david.make_withdrawal(400)
david.transfer_money(200, steph)
david.account.yield_interest()
david.display_user_balance()
