class Account:

        def __init__(self,filepath):
            self.filepath = filepath
            with open(filepath,"r") as file:
                self.balance = int(file.read())

        def withdraw(self,amount):
            with open(self.filepath,"w") as file:
                self.balance = self.balance-amount
                file.write(str(self.balance))

        def deposit(self,amount):
           with open(self.filepath,"w") as file:
               self.balance = self.balance+amount
               file.write(str(self.balance))
        def available(self):
            print("Available balance is %d "%int(account.balance))
account=Account("balance.txt")
account.withdraw(100)
account.available()
account.deposit(200)
account.available()
