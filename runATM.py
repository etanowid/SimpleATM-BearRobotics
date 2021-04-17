'''
Edriana Tanowidjaja
Inner workings of the ATM
'''
from atm import *

def runATM(user):
    # user inserts card, assuming it is the correct card
    print("Please insert your card")    
    print("Welcome " + user.seeName() + "!")
    
    # user has 3 tries to input their pin
    i = 3
    while i > 0:
        userPin = input("Please enter your pin: \n> ")
        i -= 1
        if userPin == user.pin:
            pickCheckingOrSavings(user)
            break
        else:
            print("Number of tries left: " + str(i))
            if i == 0:
                print("This account is locked. Good Bye!")
    
    
def pickCheckingOrSavings(user):
    print("What would you like to do?")
    while True:
        print("-----PICK OPTIONS-----")
        print("To manage your Checking Account, type 1")
        print("To manage your Savings Account, type 2")
        print("To quit, type 3")
        
        option = input("> ")
        option = int(option)
        
        if option == 1 or option == 2:
            # checking
            if option == 1:
                print("-----PICK OPTIONS-----")
                print("To see your Checking Account balance, type 1")
                print("To withdraw from your Checking Account balance, type 2")
                print("To deposit into your Checking Account balance, type 3")
                checkingOption = input("> ")
                try:
                    checkingOption = int(checkingOption)
                except:
                    print("-----Not a valid option. Please try again-----")
                    continue
                inChecking(user, checkingOption)
                cont = input("Would you like to do anything else? (y/n) \n> ")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    print("Good bye!")
                    break
            # savings
            elif option == 2:
                print("-----PICK OPTIONS-----")
                print("To see your Savings Account balance, type 1")
                print("To withdraw from your Savings Account balance, type 2")
                print("To deposit into your Savings Account balance, type 3")
                savingsOption = input("> ")
                try:
                    savingsOption = int(savingsOption)
                except:
                    print("-----Not a valid option. Please try again-----")
                    continue
                inSavings(user, savingsOption)
                cont = input("Would you like to do anything else? (y/n) \n> ")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    print("Good bye!")
                    break
            
        # quit
        elif option == 3:
            print("Good bye!")
            break
     
        else:
            print("-----Not a valid option. Please try again-----")



def inChecking(user, cOption):
    if cOption == 1:
        print("Checking account balance: $" + str(user.seeCheckingBalance()))
    elif cOption == 2:
        amt = input("Enter amount to withdraw in dollars (ex: 2000): \n> $")
        user.withdrawChecking(int(amt))
        print("Checking account balance is now: $" + str(user.seeCheckingBalance()))
    elif cOption == 3:
        amt = input("Enter amount to deposit in dollars (ex: 2000): \n> $")
        user.depositChecking(int(amt))
        print("Checking account balance is now: $" + str(user.seeCheckingBalance()))
    else:
        print("-----Not a valid option. Please try again-----")


def inSavings(user, sOption):
    if sOption == 1:
        print("Savings account balance: $" + str(user.seeSavingsBalance()))
    elif sOption == 2:
        amt = input("Enter amount to withdraw in dollars (ex: 2000): \n> $")
        user.withdrawSavings(int(amt))
        print("Savings account balance is now: $" + str(user.seeSavingsBalance()))
    elif sOption == 3:
        amt = input("Enter amount to deposit in dollars (ex: 2000): \n> $")
        user.depositSavings(int(amt))
        print("Savings account balance is now: $" + str(user.seeSavingsBalance()))
    else:
        print("-----Not a valid option. Please try again-----")