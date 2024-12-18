#Create a class BankAccount with private attributes balance and account_number.
#Implement methods deposit() and withdraw() to modify the balance. Ensure that the
#balance cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:   print("Insufficient funds")
    
   # @property #this property decorator makes the balance attribute read only but didnot work kinaki esle ta feri access nai garna didaina
    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

Accoun1 = BankAccount(1000, "123456")
print(Accoun1.get_balance())
Accoun1.deposit(500)
print(Accoun1.get_balance())
Accoun1.withdraw(200)
print(Accoun1.get_balance())
Accoun1.__balance = 5000000
print(Accoun1.get_balance())
    