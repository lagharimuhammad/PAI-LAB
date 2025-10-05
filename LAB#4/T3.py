class Account:
    def __init__ (self):
        self.__accNo = None
        self.__accBal = None
        self.__securityCode = None

    def initialize (self, accNo, accBal, securityCode):
        self.__accNo = str(accNo)
        self.__accBal = float(accBal)
        self.__securityCode = str(securityCode)

    def print(self):
        print(f"Account NO: {self.__accNo}")
        print(f"Account Balance: {self.__accBal}")
        print(f"Security Code: {self.__securityCode}")

a = Account()
a.initialize("866765876465", 56822, 7657)
a.print()