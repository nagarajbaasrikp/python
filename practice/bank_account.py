class BankAccount():

    def __init__(self, owner, number, balance = 1000):
        self.owner = owner
        self.number = number
        self.balance = balance
        print('Account created')

    def __str__(self):
        return f'Account Holder Name: {self.owner}\nAccount Number: {self.number}\nBalance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print('Amount Deposited')
    
    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient Balance')
        else:
            self.balance -= amount
            print('Amount withdrawn`')
    
    def show_balance(self):
        print('Account Balance: ', self.balance)
        
my_account = BankAccount('nagaraj', 1, 10000)
friend_account = BankAccount('akshay', 2)

my_account.show_balance()
my_account.deposit(1000)
my_account.show_balance()
print(my_account)
print(friend_account)

friend_account.withdraw(5000)