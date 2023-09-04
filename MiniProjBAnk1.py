from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, Account_Number, Balance):
        self.Account_Number = Account_Number
        self.Balance = Balance

    @abstractmethod
    def Deposit(self, Amount):
        pass

    @abstractmethod
    def Withdraw(self, Amount):
        pass

    def get_Balance(self):
        return self.Balance

class Checking_Account(Account):
    def __init__(self, Account_Number, Balance):
        super().__init__(Account_Number, Balance)

    def Deposit(self, Amount):
        self.Balance += Amount

    def Withdraw(self, Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
        else:
            print("Insufficient Account Balance")

class Savings_Account(Account):
    def __init__(self, Account_Number, Balance):
        super().__init__(Account_Number, Balance)

    def Deposit(self, Amount):
        self.Balance += Amount

    def Withdraw(self, Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
        else:
            print("Insufficient Account Balance")

class Business_Account(Account):
    def __init__(self, Account_Number, Balance):
        super().__init__(Account_Number, Balance)

    def Deposit(self, Amount):
        self.Balance += Amount

    def Withdraw(self, Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
        else:
            print("Insufficient Account Balance")

def main():
    accounts = {
        'C': Checking_Account('C50021336478966', 1000),
        'S': Savings_Account('S200000004245666', 2000),
        'B': Business_Account('B36922222222789', 5000)
    }

    while True:
        print("\nWelcome to Our ATM Service\n")
        Account_Type = input("Enter account type (C: Checking, S: Savings, B: Business): ").upper()
        if Account_Type not in ('C', 'S', 'B'):
            print("Invalid Account Type")
            continue

        account = accounts[Account_Type]

        print(f"Account Number: {account.Account_Number}")
        print(f"Current Balance: {account.get_Balance()}")

        Choice = input("Do you want to (D)eposit or (W)ithdraw or (Q)uit? ").upper()
        if Choice == 'Q':
            print("Thank You for Using Our ATM Service. Have a Great Day!!!!")
            break
        elif Choice == 'D':
            Amount = float(input("Enter the Amount to Deposit: "))
            account.Deposit(Amount)
            print(f"Updated Balance: {account.get_Balance()}")
        elif Choice == 'W':
            Amount = float(input("Enter the Amount to Withdraw: "))
            account.Withdraw(Amount)
            print(f"Updated Balance: {account.get_Balance()}")
        else:
            print("Invalid Choice")
        while True:
           Proceed = input("Do you want to proceed with another Transaction? (Y/N): ").upper()
           if Proceed in ('Y','N'):
                break 
           else:
               print("Invalid Input. Please Enter 'Y' or 'N' for another Transaction")

        
        if Choice == 'Q':
            break 
        else:
          print("Thank you for using our ATM service. Have a Good day!")
        
    
main()