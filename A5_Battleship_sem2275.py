# Ask player 1 for location
# Ask player 2 for location
# Store player 1 in list
# Store player 2 in separate list
# Ask player 1 for guess
# Respond with hit or miss
# Ask player 2 for guess
# Respond with hit or miss
# While loop until either player 1 or player2 list is empty
# Print winner/loser

# board = []
# print ("    A    B    C    D")
# 
# def print_board():
#     for i in range(0,4):
#         board.append(["O"] * 4)
#     for i, item in enumerate(board, start = 1):
#         print(i, item)
# print(print_board())

import time

def player_location():
    loc1 = input("Place your battleship's first coordinate:\n")
    loc2 = input("Place your battleship's second coordinate:\n")
    time.sleep(1)
    print(f"\nYou have placed your battleship at {loc1.upper()}, {loc2.upper()}.\n")
    return [loc1, loc2]

def Guess(i, ship):
    r = input(f"\nPlayer {i}, write your guess:\n")
    if r.lower() in ship:
        print("HIT")
        ship.remove(r.lower())
    else:
        print("MISS")
    return ship

def main():
    p1_ship = player_location()
    time.sleep(1)
    p2_ship = player_location()
    time.sleep(1)
    print(f"Player 1: {p1_ship}")
    print(f"Player 2: {p2_ship}")
    while True:
        p2_ship = Guess(1, p2_ship)
        if p2_ship == []:
            print("\nPlayer 1 won!")
            break
        p1_ship = Guess(2, p1_ship)
        if p1_ship == []:
            print("\nPlayer 2 won!")
            break
