q = int(input("How many quarters do you have?"))
d = int(input("How many dimes do you have?"))
n = int(input("How many nickels do you have?"))
p = int(input("How many pennies do you have?"))

total = float((0.25 * q) + (0.10 * d) + (0.05 * n) + (0.01 * p))
total = round(total, 2)
print(f"Your total for {q} quarter(s), {d} dime(s), {n} nickel(s), and {p} pennie(s) is ${total:.2f}.".format(q,d,n,p,total))
input("Are you done for today? Please type 'yes' or 'no'.")


t = (total - total * 0.10)
t = round(t, 2)
print(f"Thank you! A service fee of 10% has been deducted for using our Coinstar service. Your final amount is ${t}.".format(t))


input("Would you like to receive your money in cash or credit?")
print("Your receipt will print shortly. Have a great day!")
