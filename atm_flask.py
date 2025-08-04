# atm_web_app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated user (in real app this would come from DB)
class ATM:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def authenticate(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "✅ Deposit successful."
        return "❌ Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "❌ Invalid withdrawal amount."
        elif amount > self.balance:
            return "❌ Insufficient balance."
        else:
            self.balance -= amount
            return "✅ Withdrawal successful."

# Hardcoded user
user = ATM("1234567890", "Saksham", "5858", balance=100000)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pin = request.form.get("pin")
        if user.authenticate(pin):
            return render_template("dashboard.html", name=user.name, balance=user.check_balance(), message="Welcome!")
        else:
            return render_template("login.html", error="❌ Incorrect PIN")
    return render_template("login.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    action = request.form.get("action")
    amount = request.form.get("amount", type=float)

    if action == "balance":
        message = f"💰 Balance: ₹{user.check_balance():.2f}"
    elif action == "deposit":
        message = user.deposit(amount)
    elif action == "withdraw":
        message = user.withdraw(amount)
    else:
        message = "❌ Invalid action."

    return render_template("dashboard.html", name=user.name, balance=user.check_balance(), message=message)

if __name__ == "__main__":
    app.run(debug=True)
