# Code written by Kalen Shamy and Sophia Maron Schaeffer
# July 2, 2021

import time
import math
username = "apple72"
pin = "5254"

spend = 750
growth = 1250
reserve = 1750

print("Welcome to Sophia and Kalen's ATM!")
username_input = input("Type your username:\n")
pin_input = input("Input PIN here:\n")
while username_input != username or pin_input != pin:
    print("Invalid username or PIN. Please try again.")
    username_input = input("Type your username:\n")
    pin_input = input("Input PIN here:\n")
print(f"Login Successful.\n\nWelcome, {username}!\n\nMAIN MENU")

def coinToString(coin, amount, money):
    money = math.floor(money*100)/100
    string = ""
    if amount > 1:
        if money > 0:
            string += f"{amount} {coin}s\n"
        elif coin != "Penny":
            string += f"{amount} {coin}s"
        else:
            string += f"{amount} Pennies"
    elif amount == 1:
        if money > 0:
            string += f"{amount} {coin}\n"
        else:
            string += f"{amount} {coin}"
    return string

def create_change(money):
    """A simple function that converts dollars to quarters, dimes, nickels, and pennies. \nWith 2 arguments, returns 1 value."""
    changeStr = ""
    hundred = int(money // 100)
    changeStr += coinToString("100", hundred, money)
    money -= hundred*100
    fifty = int(money // 50)
    changeStr += coinToString("50", fifty, money)
    money -= fifty*50
    twenty = int(money // 20)
    changeStr += coinToString("20", twenty, money)
    money -= twenty*20
    ten = int(money //10)
    changeStr += coinToString("Ten", ten, money)
    money -= ten*10
    five = int(money // 5)
    changeStr += coinToString("Five", five, money)
    money -= five*5
    one = int(money // 1)
    changeStr += coinToString("One", one, money)
    money -= one*1
    q = int(money // 0.25)
    changeStr += coinToString("Quarter", q, money)
    money -= q*0.25
    d = int(money //0.1)
    changeStr += coinToString("Dime", d, money)
    money -= d*0.10
    n = int(money //0.05)
    changeStr += coinToString("Nickel", n, money)
    money -= n*0.05
    p = int(money // 0.01)
    money = 0
    changeStr += coinToString("Penny", p, money)
    return changeStr

# Kalen Shamy
def fitRequirements(question, type, typeName):
    req = input(question)
    canContinue = False
    while canContinue == False:
        try:
            req = type(req)
            canContinue = True
        except:
            req = input("\nPlease enter a valid number.\n" + question)
    return req
            
flag = True
while flag:
    choice = input("\nWhat would you like to do?\n\nA. Show my account balance\nB. Withdraw money\nC. Deposit money\nD. Cancel\n\n").upper()

    if choice == "A": #Show my account balance
        print(f"\nAccount Balance: \n\nSpend Account: ${spend:.2f}\nGrowth Account: ${growth:.2f}\nReserve Account: ${reserve:.2f}")
        time.sleep(2)
    elif choice == "B": #Withdraw money
        account = input(f"\nWhat account would you like to withdraw from?\n\nA. Spend Account: ${spend:.2f}\nB. Growth Account: ${growth:.2f}\nC. Reserve Account: ${reserve:.2f}\n\n").upper()
        while account != "A" and account != "B" and account != "C":
            account = input(f"\nSorry, \"{account}\" is not an option.\nWhat account would you like to withdraw from?\n\nA. Spend Account: ${spend:.2f}\nB. Growth Account: ${growth:.2f}\nC. Reserve Account: ${reserve:.2f}\n\n").upper()
        if account == "A": #Spend Account
            amount = fitRequirements("\nHow much do you want to withdraw?\n\n", float, "float")
            if amount <= spend:
                print(f"\nYou have withdrawn ${amount:.2f}. Your account now has ${(spend -amount):.2f}.")
                spend = spend - amount
                print("Money Withdrawn:\n\n" + create_change(amount))
            else:
                print("\nInsufficient funds. (${spend:.2f})")
        elif account == "B": #Growth Account
            amount = fitRequirements("\nHow much do you want to withdraw?\n\n", float, "float")
            if amount <= growth:
                print(f"\nYou have withdrawn ${amount:.2f}. Your account now has ${(growth -amount):.2f}.")
                growth = growth - amount
                print("Money Withdrawn:\n\n" + create_change(amount))
            else:
                print(f"\nInsufficient funds. (${growth:.2f})")
        elif account == "C": #Reserve Account
             amount = fitRequirements("\nHow much do you want to withdraw?\n\n", float, "float")
             if amount <= reserve:
                print(f"\nYou have withdrawn ${amount:.2f}. Your account now has ${(reserve - amount):.2f}.")
                reserve = reserve - amount
                print("Money Withdrawn:\n\n" + create_change(amount))
             else:
                print(f"\nInsufficient funds. (${reserve:.2f})")
    elif choice == "C": #Deposit money
        account = input(f"\nWhat account would you like to deposit money into?\n\nA. Spend Account: ${spend:.2f}\nB. Growth Account: ${growth:.2f}\nC. Reserve Account: ${reserve:.2f}\n\n").upper()
        while account != "A" and account != "B" and account != "C":
            account = input(f"\nSorry, \"{account}\" is not an option.\nWhat account would you like to withdraw from?\n\nA. Spend Account: ${spend:.2f}\nB. Growth Account: ${growth:.2f}\nC. Reserve Account: ${reserve:.2f}\n\n").upper()
        if account == "A": #Spend Account
            amount = fitRequirements("\nHow much do you want to deposit?\n\n", float, "float")
            if amount > 0:
                print(f"\nYou have deposited ${amount:.2f}. Your account now has ${(spend + amount):.2f}.")
                spend = spend +amount
            else:
                print("\nInsufficient funds. (${spend:.2f})")
        elif account == "B": #Growth Account
            amount = fitRequirements("\nHow much do you want to deposit?\n\n", float, "float")
            if amount > 0:
                print(f"\nYou have deposited ${amount:.2f}. Your account now has ${(growth + amount):.2f}.")
                growth = growth + amount
            else:
                print(f"\nInsufficient funds. (${growth:.2f})")
        elif account == "C": #Reserve Account
             amount = fitRequirements("\nHow much do you want to deposit?\n", float, "float")
             if amount > 0:
                print(f"\nYou have deposited ${amount:.2f}. Your account now has ${(reserve + amount):.2f}.")
                reserve = reserve +amount
             else:
                print(f"\nInsufficient funds. (${reserve:.2f})")
    elif choice == "D": #Cancel
        run = False
        print("\nThank you for your time. Have a great day!")
        break
    else:
        choice = input(f"\nSorry, {username}. \"{choice}\" is not an option. What would you like to do?\n\nA. Show my account balance\nB. Withdraw money\nC. Deposit money\nD. Cancel\n").upper()

