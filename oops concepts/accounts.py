class MyBank:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc=acc
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs.{amount}: Credit to Your Account")
        print(f"Total Balance : {self.get_balance()}")
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs.{amount} Debit to Your Account")
        print(f"Total Balance : {self.get_balance()}")
    def get_balance(self):
        print(self.balance)
Acc1=MyBank(1130,242424)
print(Acc1.acc)
print(Acc1.balance)

Acc1.get_balance()





