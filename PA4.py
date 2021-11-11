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
    x=0
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
            print(name)
        elif (suit == "d"):
            name = n + " of diamonds"
            print(name)
        elif (suit == "s"):
            name = n + " of spades"
            print (name)
        else:
            name = n + " of hearts"
            print (name)
        x+=1


#def show_hand():
    #y=0
    #for i in user:
      #  name(user[y])
       # y+=1
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
    return total

def starting_draw(deck, user):
    for y in range (2):
        card = deck.pop(0)
        user.append(card)
        # print(user)
        #card = name(user)
    name(user)
    total = calc_total(user)
    return total
def draw(deck, user):
    card = deck.pop(0)
    user.append(card)
    name(user)
    calc_total(user)
    return total

deck = []
user = []
dealer = []
shuffle()
#print (deck)
starting_draw(deck,user)
total = calc_total(user)
dtotal=0
winner = 0
while (winner == 0):
    choice = input("Would you like to draw another card? ")
    while (total < 21 and choice == "yes"):
        total=calc_total(user)
        draw(deck, user)
        if (total > 21):
            print ("Your total is greater than 21")
            print("Your total: ", total)
            print("Dealer's total: ", dtotal)
            winner = 1
        choice = "no"
        choice = input("Would you like to draw another card? ")
    print("dealers deck: ")
    while (winner == 0):
        starting_draw(deck, dealer)
        dtotal=calc_total(dealer)
        while (dtotal <17):
            draw (deck, dealer)
            dtotal= calc_total(dealer)
        if (dtotal > 21 or total>=dtotal):
            print("Your total: ", total)
            print("Dealer's total: ", dtotal)
            winner = 2
        else:
            print ("The dealer had a better hand than you")
            print("Your total: ", total)
            print("Dealer's total: ", dtotal)
            winner = 1

if (winner == 1):
    print("You lose")
else:
    print ("You win!")


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