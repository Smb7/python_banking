from os import name
from banking_pkg import account


# Task 2: Registration
print("          === Automated Teller Machine ===          ")
name = input('Enter name to register ')
pin = input('Enter pin ')
balance = float()
print(name, "has been registered with a starting balacnce of $", balance)

# Task 3: log in and prompt menu 
print("          === Automated Teller Machine ===          ")
print("Login to access banking ")
while True:
    name_to_validate = input('enter name ')
    pin_to_validate = input('enter pin ')
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
    else:
        print('invalid credentials')
        break
# ATM Menu (prompt)
    def atm_menu(name):
        print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Task 3: ATM Menu user input
    while True:
        atm_menu(name)
        option = input("choose an option ")
        if option == "1":
            account.show_balance(balance)
        elif option == "2":
            balance = account.deposit(balance)
        elif option == "3":
            balance = account.withdraw(balance)
        elif option == "4":
            account.logout(name)
            break
        else:
            print('logout')
            break
