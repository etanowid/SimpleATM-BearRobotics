'''
Edriana Tanowidjaja
Create an Account class for each ATM user
'''
class Account:
    # Construct an Account object
    def __init__(self, accNumber, name, pin, checkingBalance, savingsBalance):
        self.accNumber = accNumber
        self.name = name
        self.pin = pin
        self.checkingBalance = checkingBalance
        self.savingsBalance = savingsBalance
    
    def seeAccNumber(self):
        return self.accNumber

    def seeName(self):
        return self.name

    def seeCheckingBalance(self):
        return self.checkingBalance
 
    def withdrawChecking(self, amount):
        self.checkingBalance -= amount
 
    def depositChecking(self, amount):
        self.checkingBalance += amount
 
    def seeSavingsBalance(self):
        return self.savingsBalance
 
    def withdrawSavings(self, amount):
        self.savingsBalance -= amount
 
    def depositSavings(self, amount):
        self.savingsBalance += amount
 

 
