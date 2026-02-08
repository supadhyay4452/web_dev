class BankAccount:
    def __init__(self, balance):
        self .__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("Amount deposited")
        else:
            print("invalid deposit")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount
            print("withdrawal successfull")
        else:
            print("insufficient balnce")

    def get_balance(self):
        return self.__balance

acc=BankAccount(2000)
acc.deposit(500)
acc.withdraw(900)
print(acc.get_balance())     

