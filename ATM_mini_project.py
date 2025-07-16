class ATM:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def authenticate(self):
        enteredPin = input("Enter your PIN: ")
        if enteredPin == self.pin:
            print("Authentication successful!\n")
            return True
        else:
            print("Incorrect PIN. Access denied.\n")
            return False

    def checkBalance(self):
        print(f"Available Balance: {self.balance}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("deposited successfully:\n")
        else:
            print("Invalid deposit amount.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.\n")
        elif amount > self.balance:
            print("Insufficient balance.\n")
        else:
            self.balance -= amount
            print("amout withdrawn successfully.\n")

    def options(self):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.checkBalance()
            elif choice == '2':
                amt = float(input("Enter amount to deposit: "))
                self.deposit(amt)
            elif choice == '3':
                amt = float(input("Enter amount to withdraw:"))
                self.withdraw(amt)
            elif choice == '4':
                print("Thank you")
                break
            else:
                print("Invalid option. Try again.\n")


custm = ATM("1234567890", "Saksham", "5858",balance=100000)

if custm.authenticate():
    custm.options()