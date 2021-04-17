'''
Edriana Tanowidjaja
Program starts here.
The inner workings are on atm.py and runATM.py to account for abstraction and modularity
'''

from atm import *
from runATM import *

if __name__ == "__main__":
    # Account(acct number, name, pin, checking, savings)
    # betty is an existing user
    # When run, input pin = 1234
    betty = Account('12344321', 'Betty Beep Boop', '1234', 400, 5000)
    runATM(betty)


    """ # for testing
    print(betty.seeAccNumber())         # '12344321'
    print(betty.seeName())              # 'Betty Beep Boop'

    print(betty.seeCheckingBalance())   # 150
    betty.withdrawChecking(50)
    print(betty.seeCheckingBalance())   # 100
    betty.depositChecking(100)
    print(betty.seeCheckingBalance())    # 200

    print(betty.seeSavingsBalance())    # 4000
    betty.withdrawSavings(500)
    print(betty.seeSavingsBalance())    # 3500
    betty.depositSavings(100)
    print(betty.seeSavingsBalance())    # 3600  
    """