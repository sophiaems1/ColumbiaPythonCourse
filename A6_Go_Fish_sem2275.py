# Sophia Maron Schaeffer and Kalen Shamy
# Assignment 6: Go Fish 
 
import random
 
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['d','c','h','s']
 
playAgain = True

def uinput(string):
    return input(string + " ")
 
def replaceStrAtIndex(string, replaceVal, index): # workaround for string[index] = replaceVal
    returnString = ""
    for i in range(len(string)):
        if i != index:
            returnString += string[i]
        else:
            returnString += replaceVal
    return returnString
 
def listOfRanks(hand):
    returnStr = ""
    for rank,suits in hand.items():
        hasCard = suits != []
        if hasCard == True:
            returnStr += rank + ", "
    returnStr = replaceStrAtIndex(returnStr, "", len(returnStr)-1)
    returnStr = replaceStrAtIndex(returnStr, "", len(returnStr)-1)
    return returnStr
 
def viewCards(hand):
    printStr = ""
    for rank, suits in hand.items():
        if suits != []:
            printStr += rank + ": "
            for suit in suits:
                printStr += suit + " "
            printStr += "\n"
    print(printStr)
 
def pop(list_, position):
    item = list_[position]
    newList = []
    for i in range(len(list_)):
        if i != position:
            newList.append(list_[i])
    return item, newList
 
def drawCard(deck, hand):
    rank = ranks[random.randint(0,len(ranks)-1)]
    while deck[rank] == []:
        rank = ranks[random.randint(0,len(ranks)-1)]
    try:
        suit, deck[rank] = pop(deck[rank],random.randint(0,len(deck[rank])-1))
    except:
        print(deck,rank)
    hand[rank].append(suit)
    return rank
 
while playAgain == True:
    deck = {}
    hands = [{},{}]
    sets = []
    playerPoints = [0,0]
 
    for rank in ranks:
        deck[rank] = suits
        hands[0][rank] = [] # Player 1 -- Index = Player# - 1
        hands[1][rank] = [] # Player 2
        
    for i in range(7): # Give player cards
        drawCard(deck, hands[0])
    for i in range(7):
        drawCard(deck, hands[1])
 
    while len(sets) != 13:
        for player in range(1,3):
            target = 0
            if player == 1:
                target = 2
            else:
                target = 1
            print(f"Player {player}:\n\nYour deck:")
            viewCards(hands[player-1])
            rankToAsk = uinput(f"What card rank do you want to ask for?").upper()
            while True:
                try:
                    if hands[player-1][rankToAsk] == []:
                        raise Exception
                    break
                except:
                    rankToAsk = input(f"You can only ask for a card that you have. What card rank do you want to ask for? Ranks:\n{listOfRanks(hands[player-1])}\n").upper()
            suitsTargetHas = hands[target-1][rankToAsk]
            if len(suitsTargetHas) != 0:
                hands[target-1][rankToAsk] = []
                print(f"Player {target} has {len(suitsTargetHas)} {rankToAsk}'s. {rankToAsk}'s added to your hand.")
                for suit in suitsTargetHas:
                    hands[player-1][rankToAsk].append(suit)
                if len(hands[player-1][rankToAsk]) == 4:
                    hands[player-1][rankToAsk] = []
                    sets.insert(ranks.index(rankToAsk), rankToAsk)
                    playerPoints[player-1] += 1
                    print(f"You have gotten 4 {rankToAsk}'s. Removed from your hand. You now have {playerPoints[player-1]} set(s) created.")
            else:
                print(f"Player {target} does not have any {rankToAsk}'s. Go fish!")
                rankFished = drawCard(deck, hands[player-1])
                if len(hands[player-1][rankFished]) == 4:
                    hands[player-1][rankFished] = []
                    sets.insert(ranks.index(rankFished), rankFished)
                    playerPoints[player-1] += 1
                    print(f"You have gotten 4 {rankFished}'s. Removed from your hand. You now have {playerPoints[player-1]} sets created.")
            if len(sets) == 13:
                print(f"Congrats, Player {player}, you have won with {playerPoints[player-1]} sets!")