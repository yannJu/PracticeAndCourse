class BackAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingAccount(BackAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate

    def setInterest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def getInterest_rate(self):
        return self.interest_rate

    def saveRate(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BackAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.charge = 1000

    def withdraw(self, amount):
        return BackAccount.withdraw(self, amount + self.charge)

a1 = SavingAccount("이아연", 123456789, 10000, 0.05)
a1.saveRate()
print("a1의 잔액은 : ", a1.balance)

a2 = CheckingAccount("이연주", 2030203, 2000000)
a2.withdraw(1000000)
print("a2의 잔액은 : ", a2.balance)