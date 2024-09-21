#!/usr/bin/python3
import itertools
import collections
import random

class Card():
    def __init__(self,face:str,suit:str,value:int = None) -> None:
        self.face = face
        self.suit = suit 
        self.value = self.card_value() 

    def card_value(self):
        if self.face in {'J','Q','K'}:
            self.value = int(10)
        elif self.face == "A":
            self.value = int(11)
        else:
            self.value = int(self.face)        
        return self.value    

    def tuplecard(self) -> tuple[str,str,int]:
        return tuple([self.face,self.suit,self.card_value()])

    def __str__(self) -> str:
        return f"{self.face},{self.suit},{self.card_value()}"

class Stack():
    def __init__(self) -> None:
        self.stacklist = []
 
    def appendcard(self, card:tuple[str,str]) -> None:
        return self.stacklist.append(card)

    def extendstack(self,cards):
        return self.stacklist.extend(cards)

    def list_by_cardclass(self) -> None:
        return [Card(f,s) for f,s in self.stacklist]
    
    def sum_cards(self):
        cards = [Card(f,s) for f,s in self.stacklist]
        self.cardssum = sum([card.value for card in cards])
        if self.ace_in_stack and self.cardssum > 21:
        #if any(card.face == "A" for card in cards) and self.cardssum > 21:
            self.cardssum -= 10
                
            #self.cardssum = self.cardssum - 10
        return self.cardssum 
        # def sum_cards(self, cards):
        #     self.cardssum = sum([card.value for card in cards])
        #     return self.cardssum

    def getcards(self):
        return self.stacklist

    def rmcard_frmstack(self, n = 1) -> list[tuple[str,str]]:     
        try:
            #return self.stacklist.pop()
            return [self.stacklist.pop() for count in range(1,n + 1)]
             
        except IndexError as err:
            print("no cards left in dec`k")
            raise
    
    def length_stack(self):
        return len(self.stacklist)

    def clearstack(self) -> None:
        self.stacklist.clear()

    def ace_in_stack(self):
        if any(card.face == "A" for card in self.list_by_cardclass()): 
            return True 

    def deque_deck(self) -> None:
        return collections.deque(self.stacklist)

    def cards_remain(self) -> True:
        if len(self.stacklist) > 0:
            return True 
    
    def __str__(self):
        return f"Holds the cards: {self.stacklist}"

class Deck(Stack):
    def __init__(self):
        super().__init__()
        self.create_deck()
    
    def create_deck(self) -> None:
        self.stacklist.clear()
        face_list: list[str] = [ "A", "J", "Q", "K"] + [str(i) for i in range(2,10+1)]
        suit_list: list[str] = ["Clubs", "Hearts", "Spades", "Diamonds"]
        self.stacklist = [cards for cards in list(itertools.product(face_list,suit_list))]
        #self.stacklist = [Card(face,suit) for face,suit in list(itertools.product(face_list,suit_list))]
        #self.stacklist.append(card.tuplecard())
        random.shuffle(self.stacklist)  
        return self.stacklist

    def multiple_deck(self, n: int = 2) -> None:
        self.stacklist : list[tuple[str,str]] | collections.deque[str,str] = [self.create_deck() for i in range(1,n + 1)]   
        return self.stacklist
           
    def __str__(self) -> str:
        return f"Cards left in deck: {self.stacklist}"
    
class Player():
    def __init__(self,name: str = "player") -> None:
        self.name = name 
        self.set_name()
         
    def set_name(self) -> None:
        self.name: str = input("Enter name: ")
    
    def p_input(self,i):
        _ = input(i)
        if _ in {"Q","q"}:
            exit("Quiting game as you commanded!")
        return _
    
    def __str__(self):
        return f"{self.name}"

class Money():
    def __init__(self,start:int):
        self.start = start
        self.running = []
        self.__run_start()
       
    def __run_start(self) -> list[int]:
        self.running.append(self.start)

    def getlast_runningint(self) -> int:
        return int(self.running[-1])
    
    def have_money(self) -> True:
        if self.running[-1] > 0:
            return True 

    def appnd_run(self,i:int):
        return self.running.append(i) 
    
    def intrsum_newrun(self) -> list[int]:
        itrsum = sum(self.running) 
        self.running.clear()
        return self.running.append(itrsum)
        
    def inrange(self,num:int) -> int:
        return num in range(0,max(self.running)+1) 

    def __repr__(self) -> str:
        return f"[{self.start},{self.running}]"

    def __str__(self) -> str:
        return f"Your Wallet stolen from Vox far-right party contains  ${self.running[-1]}\n"

class Game():
    def __init__(self, wallet, deck, player_hand,dealer_hand,player):
        self.wallet = wallet 
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        #self.card = card
        #self.stack = stack 
        self.deck = deck
        self.player = player
        #self.player_hand = []
        self.cardssum = 0        

    def greet(self):
        print(f'''
        Welcome {player.name} to Black Jack the Ripper!!! 
        It's like BlackJack without the complexities of splits,double downs, and other comforts
        that didn't exist during Jack the Rippers terror.  
        ''')

    def rules(self):
        request_rules = input("Press (y) if you want the game rules, or any other key to proceed: \n")
        if request_rules in {"y","Y"}:
            print('''
            Player wagers a bet before the first roll – the come-out roll. 
            If the come-out roll is a 7 or 11, then the player wins the wager 
            immediately.Conversely, if the come-out roll is a 2, 3 or 12, the 
            player “craps-out” and loses wager. If the come-out roll is any 
            other numer (4, 5, 6, 8, 9 or 10) then that specific number 
            becomes the player’s point and the player continues to roll the dice 
            until either the point number is rolled or a 7 or 11 is rolled. 
            If the point number is rolled, then the player wins the wager. The 
            player loses the wager if either 7 or 11 is rolled before the point.
            The game repeats with a new round (i.e comeout roll) until the 
            player quits or loses all money.\n''') 
        pass

    def game_play(self):
        while wallet.have_money():
            return True    
        
    def start(self):     
        #self.greet()
        print(str(wallet))
    
    def place_bet(self):  
        while True:
            bet = player.p_input("enter wager: ")
            try:
              bet = int(bet)
              #assert 0 <= bet <= wallet.getlast_runningint()
              assert wallet.inrange(bet)
            except ValueError:
              print("only integers accepted\n")
            except AssertionError:
              print("must enter value within wallet\n")
            else:
                break
        return bet
    
    def confirm_hit(self):
        return player.p_input("press (y) to ask for another card, (q) to quit game, or any other key to stand with current cards:  ##\n")
    
    def blackjack(self,pass_sum):
         if pass_sum == 21:
            return True 
    
    def bust(self,pass_sum):
        if pass_sum > 21:
            return True

    def h1_gt_h2(self,pass_sum1,pass_sum2):
        if pass_sum1 > pass_sum2 and not self.bust(pass_sum1):
            return True
    
    def storesums_as_tuple(sum1,sum2):
        return tuple([sum1,sum2])

    def win(self,bet):     
        print("win")
        return wallet.appnd_run(bet)
      
    def lose(self,bet):
        print("lose")
        return wallet.appnd_run(-1 * bet)


card1 = Card("10","Club")
#print(card1.face) 
print(card1.tuplecard())
#stack = Stack()
#stack.appendcard(card1.tuplecard())
#print(stack.getcardlist())
deck = Deck()
wallet = Money(200)
player = Player("p1")

player_hand = Stack()
dealer_hand = Stack()
game = Game(deck,wallet,player_hand,dealer_hand,player)
## test decksg
print(""" Testing decks \n""")
print()
#deck.create_deck()
print(deck.stacklist)
player_hand.extendstack(deck.rmcard_frmstack(2))
player_hand.extendstack(deck.rmcard_frmstack())
print(player_hand)
#player_hand = player_hand.list_by_cardclass()

#player_hand = [Card(f,s) for f,s in player_hand]

#psum = game.sum_cards([game.card_values(card) for card in player_hand.list_by_cardclass()])
#player_hand.sum_cards(player_hand.list_by_cardclass())
player_hand.sum_cards()
dlsum = sum([game.card_values(card) for card in dealer_hand.list_by_cardclass()])
if player_hand.length_stack() == 2:
    print(player_hand.cardssum)
if game.blackjack(player_hand.cardssum):
    print("BlackJack")
else:
    print("no")

#game.storesums_as_tuple(player_hand.cardssum, dealer_hand.cardssum)
#player_hand.appendcard(deck.rmcard_frmstack())
player_hand.extendstack([('A', 'Clubs')])
print(player_hand)
player_hand.sum_cards()
#if player_hand.ace_in_stack() and player_hand.cardssum > 21:
        
#player_hand.sum_cards(player_hand.list_by_cardclass())
print(player_hand.cardssum)
#card = Card(card[0],card[1])
#    print(card)
#pvalues = list(zip(*phand))[2m]
#print(pvalues)




print("""testing gameplay""")
print()
#player = Player("p1")

def main():
    deck = Deck()
    wallet = Money(200)
    player = Player("p1")
    player_hand = Stack()
    dealer_hand = Stack()
    game = Game(deck,wallet,player_hand,dealer_hand,player)

    player_hand.extendstack(deck.rmcard_frmstack(2))
    dealer_hand.extendstack(deck.rmcard_frmstack(2))
    scores = game.storesums_as_tuple(player_hand.sum_cards(),dealer_hand.sum_cards())
    print(f"{player.name}: {player_hand.sum_cards()} hand {player_hand}")
    print(f"Jack 'The Ripper' Dealer: {dealer_hand.sum_cards()} hand {dealer_hand}")
    


    if game.blackjack(player_hand.cardssum) and not game.blackjack(dealer_hand.cardssum):
        print("win")     

    while not game.blackjack(player_hand.cardssum) or game.blackjack(dealer_hand.cardssum):
        if game.confirm_hit() in {'y','Y'}:
            player_hand.extendstack(deck.rmcard_frmstack())
            print(player_hand.sum_cards())
        if game.h1_gt_h2(player_hand.cardssum,dealer_hand.cardssum):
            print("greater")

        if game.bust(player_hand.cardssum):
            print("bust")
            break 
    print("lose")

main()
#deck1.create_deck()
#deck1.deque_deck()
#print(deck1.rmcard_frmdeck())
#print(deck1.remaining_deck())
#print(deck1.multiple_deck())
#deck_pl = Deck()
#deck_pl.createblank_deck()
#stack = Stack()
#stack.appendcard(card1)
#print(stack.appendcard(card1))
#def ph(deck1,deck_pl):
#    x = deck1.
#    return [deck_pl.appendcard(i) for i in x]
#
#ph(deck1,deck_pl)
