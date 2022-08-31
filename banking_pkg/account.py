def show_balance(balance):
    balance 
    print("current balance ", balance)
    return balance
def deposit(balance):
    deposit_amount = float(input("Enter amount to deposit: "))
    balance = balance + deposit_amount
    print("current balance ", balance)
    return balance
def withdraw(balance):
    withdraw_amount = float(input("Enter amount to withdraw: "))
    balance = balance - withdraw_amount
    print("current balance ", balance)
    return balance
def logout(name):
    print("Goodbye ", name)

