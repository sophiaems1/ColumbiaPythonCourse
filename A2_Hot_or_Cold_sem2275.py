code = 25
print("Welcome to Sophia's Hot or Cold game!")
print("You have a total of 10 tries to figure out the secret number between 1 and 100 (only integers).")
x = int(input("Enter a guess:"))
guesses = 1

while x != code:
    if x >= 0 and x < 15:
        print("You're warm!")
        x = int(input("Enter a new guess (so close!): "))
        guesses = guesses + 1
    if x > 35 and x <= 50:
        print("You're warm!")
        x = int(input("Enter a new guess (so close!): "))
        guesses = guesses + 1
    if x >= 15 and x <= 35:
        print("You're on fire!")
        x = int(input("Enter a new guess (YOU GOT THIS!!): "))
        guesses = guesses + 1
    if x > 50 and x <= 75:
        print("You're cold!")
        x = int(input("Enter a new guess (try smaller numbers): "))
        guesses = guesses + 1 
    if x > 75:
        print("You're freezing cold!")
        x = int(input("Enter a new guess (think MUCH smaller): "))
        guesses = guesses + 1
    elif guesses == 10:
        print(f"Sorry, you lost the game. The correct number was: {code}.")
        break
    
print()
print()
if x == 25:
    print("You're amazing! Great job, you found Sophia's secret code!")
print()
print(f"It took you {guesses} guesses!".format(guesses))

