
# 🏧 ATM Simulation – Mini Project in Python

This mini project simulates an **ATM Machine** using Python’s Object-Oriented Programming (OOP) concepts. It includes core ATM functionalities like user authentication, balance inquiry, deposits, and withdrawals.

---

## 🚀 Features

- 🔐 PIN-based authentication
- 💰 Balance check
- 💸 Deposit money
- 🏧 Withdraw money
- 🔁 Repeated transactions via a menu
- ✅ Basic input validation

---

## 🛠️ How It Works

The `ATM` class encapsulates all the logic. Here's what it does:

- `__init__()` – Initializes the account with account number, user name, PIN, and an optional balance.
- `authenticate()` – Verifies the PIN.
- `checkBalance()` – Displays current balance.
- `deposit(amount)` – Adds money to the account.
- `withdraw(amount)` – Withdraws money if funds are sufficient.
- `options()` – Shows a simple menu to perform transactions.

---

## 📌 Sample Run

```python
Enter your PIN: 5858
Authentication successful!

Check Balance

Deposit

Withdraw

Exit
Choose an option (1-4): 1
Available Balance: 100000
```

---

## 💡 How to Use

You can change the default account info like this:

```python
custm = ATM("your_account_no", "YourName", "YourPIN", balance=your_starting_balance)
```

---

## ✅ Requirements

- Python 3.x
- No external libraries required

---

## 🌐 Flask Web Version (Optional)

If you're using the Flask-based web version of the ATM simulator:

### 🔧 Setup & Run

1. Make sure you have Flask installed:

```bash
pip install flask
```

2. Run the Flask app (example: `atm_flask.py`):

```bash
python atm_flask.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, or share with proper attribution.

---

## 🙌 Acknowledgments

Created using Python and OOP Concepts as part learning Data Science

---

## Author

Developed by Saksham Sharma
