# Programmers: Peter Hope
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: to draw another card or not
# Program Outputs: new card, current hand total, users and dealers final hands and totals, outcome/winner
import random

def shuffle():
    for i in range(1,14):
        i =str(i)
        a = i +" c"
        deck.append(a)
    for i in range(1,14):
        i =str(i)
        a = i +" d"
        deck.append(a)
    for i in range(1,14):
        i =str(i)
        a = i +" s"
        deck.append(a)

    for i in range(1,14):
        i =str(i)
        a = i +" h"
        deck.append(a)
    random.shuffle(deck)

def name(hand):
    x=-1
    #y=int(0)
    for i in hand:
        card = hand[x]
        num, suit = card.split()
        num = int(num)
        if (num == 1):
            n = "Ace"
        elif (num == 11):
            n = "Jack"
        elif (num == 12):
            n = "Queen"
        elif (num == 13):
            n = "King"
        else:
            n = str(num)
        if (suit == "c"):
            name = n + " of clubs"
        elif (suit == "d"):
            name = n + " of diamonds"
        elif (suit == "s"):
            name = n + " of spades"
        else:
            name = n + " of hearts"
        x+=1
    print (name)

def show_hand():
    y=0
    for i in user:
        name(user[y])
        y+=1
        #print ("h", h)

def calc_total(hand):
    x = 0
    total = 0
    # y=int(0)
    for i in hand:
        card = hand[x]
        num, suit = card.split()
        num = int(num)
        total += num
        x+=1
    print ("total: ",total)



deck = []
user = []
shuffle()
print (deck)
#user = draw(user)
for y in range(4):
    card = deck.pop(0)
    user.append(card)
    #print(user)
    card = name(user)
calc_total(user)


show_hand()

#print (card)
#print (deck)


#create deck and shuffle it
#draw user 2 cards
#print deck and total
#ask if user wants another card
    #if yes
        #draw another card
        #show deck and total
        #if over 21, end game
        #show loss
    #if no move on
#dealer draws 2 cards
    #show deck and total
    #if less than 17
        #draw again
        #show deck and total
    #if over 21 end game
    #show win
# once between 17 and 21
    #compare hands
    #bigger hand wins
    #show win/loss