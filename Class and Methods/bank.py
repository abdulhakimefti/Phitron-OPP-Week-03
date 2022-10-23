class Bank :
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 50000
    def get_balance(self):
        return self.balance
    def withdraw (self,amount):
        if amount<self.min_withdraw:
            return 'No money for you'
        elif amount > self.max_withdraw:
            return f'you crossed max limit:{self.maxwithdraw}'
        elif amount>self.balance:
            return "You have not sufficient balance"
        else :
            self.balance = self.balance-amount
            return f'here is your money {amount}'

my_bank = Bank(40000)
reply = my_bank.withdraw(100)
print(reply)
reply = my_bank.withdraw(2000)
print(reply)
print(my_bank.balance)