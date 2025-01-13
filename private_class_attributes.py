class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount methods can access self._balance, but code outside of
        # this class should not:
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
        if amount <= 0:
            return  # dont allow negative "deposits"
        if amount >= 0:
            self._balance += amount
            with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
                ledgerFile.write('Deposit ' + str(amount) + '\n')
                ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance <= 0 or self._balance < amount or amount < 0:
            return  # not enough in amount, balance is smaller then amount of amount is negative
        else:
            self._balance -= amount
            with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
                ledgerFile.write('Withdraw ' + str(amount) + '\n')
                ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice')
acct.deposit(120)
acct.withdraw(40)
print(acct._balance)

acct._balance = 1000000000  # you can change the "private" attributes directly
acct.withdraw(1000)

acct._name = 'Bob'  # Now we're modifying Bob's account ledger!
acct.withdraw(1000)  # This withdrawal is recorded in BobLedger.txt!