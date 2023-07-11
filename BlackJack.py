import random
game_on = True
c=''
su = 0
su_2 = 0
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#CHECKS VALUE FOR 21
def checker_21(summ,name):
    global game_on
    global su_2
    if summ == 21:
        print("{} WINS".format(name))
        if name == player_one.name:   
            player_one.bank+=bets
        else:
            player_one.bank-=bets
        print("PC hand value was {}".format(su_2))
        print("{} hand value was {}".format(player_one.name,su))
        game_on = False
    elif summ < 21:
        global c
        if c == "Hit":
            player_pc.hand.append(new_deck.hit())
            su_2+=player_pc.hand[-1].value
            c=''
        elif c == "Stay":
            player_pc.hand.append(new_deck.hit())
            su_2+=player_pc.hand[-1].value
            c=''
        else:
            pass
    else:
        print("{} has busted! {} lost!".format(name,name))
        if name == player_one.name:         
            player_one.bank-=bets
        else:
            player_one.bank-=bets
        print("PC hand value was {}".format(su_2))
        print("{} hand value was {}".format(player_one.name,su))
        game_on = False

#Class for a card
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

#Class for a deck
class Deck():
    def __init__(self):
        
        self.all_cards = []
        
        for i in suits:
            for j in ranks:
                created_card = Card(i,j)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def give_one(self):
        return self.all_cards.pop(0)
    
    
    def give_two(self):
        a = [self.all_cards.pop(0)]
        a.append(self.all_cards.pop(0))
        return a
    
    def hit(self):
        return self.all_cards.pop(0)
    
#Class for a player
class Player():
    def __init__(self,name,bank):
        self.name = name
        self.bank = bank
        self.hand = []
        
    def remove(self):
        return self.hand.pop(0)      
    def add(self,hit_card):
        self.hand.append(hit_card)
    
#Class for the pc
class PC():
    def __init__(self,name):
        self.name = name
        self.hand = []
        

#BETTING LOGIC
new_deck = Deck()
new_deck.shuffle()
player_one = Player("Surya",5000)
player_pc = PC("PC")
while True:
    aa = int(input("Hello! Welcome to BlackJack! How much would you like to bet? : "))
    if player_one.bank < aa:
        print("Please try again!")
    else:
        bets = aa
        break
    
#ADDING CARDS TO PLAYER AND PC       
player_one.hand.extend(new_deck.give_two())
player_pc.hand.append(new_deck.give_one())

#ACE HANDLER
for i in player_one.hand:
    if i.rank == "Ace":
        b = int(input("One card is an ace. Would you like its value to be 1 or 11? : "))
        i.value = b
        su+=i.value
    else:
        su+=i.value
        continue
    
    
#ADDING SUM OF PC
for i in player_pc.hand:
    su_2+=i.value

#GAME LOOP
while game_on == True:
    if su >= 21:
        checker_21(su,player_one.name)
        break
    elif su_2 >= 21:
        checker_21(su_2,player_pc.name)
        break
    elif (su == su_2) >= 21:
        print("You both suck")
        break
    
    c = input("Your hand value is {}. Would you like to Hit or Stay? : ".format(su))
    if c == "Hit":
        player_one.hand.append(new_deck.hit())
        if player_one.hand[-1].rank == "Ace":
            b = int(input("One card is an ace. Would you like its value to be 1 or 11? : "))
            player_one.hand[-1].value = b 
        su+=player_one.hand[-1].value
        checker_21(su,player_one.name)
    elif c == "Stay":
        checker_21(su_2,player_pc.name)      
        game_on = False
        
#STUPID EXCEPTION HANDLER
if su_2 > 21:
    checker_21(su_2,player_pc.name)

elif su_2 == 21:
    checker_21(su_2,player_pc.name)
    
#STAY CONDITION EXCEPTION HELPER   
if (su < 21 and su_2 < 21):     
    if su > su_2:
        print("{} wins!!!".format(player_one.name))
        print("PC hand value was {}".format(su_2))
        print("{} hand value was {}".format(player_one.name,su))
        player_one.bank += bets
    elif su_2 > su:
        print("{} loses lmao".format(player_one.name))
        print("PC hand value was {}".format(su_2))
        print("{} hand value was {}".format(player_one.name,su))
        player_one.bank -= bets
    else:
        print("Tie")
    