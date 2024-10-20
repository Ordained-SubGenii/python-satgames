#!/usr/bin/python3
import os
import itertools
import random
import time
import termcolor
import re 

class ColoredText():
    def __init__(self, text: str, color: str) -> None:
        self.text = text
        self.color = color

    def __str__(self) -> str:
        return termcolor.colored(self.text,self.color)

class Money():
    def __init__(self,start:int) -> None:
        self.start = start
        self.running_balance = []
        self.__run_start()
       
    def __run_start(self) -> None:
        '''initates a running_balance value for money object based on provided start value argument'''
        self.running_balance.append(self.start)

    def getlast_running_balanceint(self) -> int:
        '''return last value in running_balance money list'''
        return int(self.running_balance[-1])
    
    def have_money(self) -> True:
        '''boolean value whether running_balance is greater than 0'''
        if self.running_balance[-1] > 0:
            return True 

    def appnd_run(self,increment:int) -> list:
        '''appends an increment int argument to running_balance'''
        return self.running_balance.append(increment) 
    
    def calc_new_running_balance(self) -> list:
        '''take sum of values in running_balance list, reset list to empty, and start new list containing previou sum'''
        itrsum: int = sum(self.running_balance) 
        self.running_balance.clear()
        return self.running_balance.append(itrsum)
        
    def inrange(self,num:int) -> int:
        '''evaluate if provided number argument is greater than 0 and within range of running_balance'''
        return num in range(1,max(self.running_balance)+1) 

    def __repr__(self) -> str:
        return f"[{self.start},{self.running_balance}]"

    def __str__(self) -> str:
        return f"!!! You have {ColoredText({self.running_balance[-1]},"light_red")} {ColoredText("blood drops remaining !!!", "red")}\n"

class Player():
    def __init__(self,name = None) -> None:
        self.name = name 
        self.__set_name()
         
    def __set_name(self) -> str:
        '''prompt user for name and return player's name to caller'''
        self.name: str = input("Enter name: ")
        return self.name

    def p_input(self,user_input: str) -> any:
        '''take and return user/player input. quit program if Q or q entered'''
        _ = input(user_input)
        if _ in {"Q","q"}:
            exit("Quiting game as you commanded!")
        return _
    
    def __str__(self) -> str:
        return f"{self.name}"

class Dealer(Player):
    def __init__(self,name = "dealer") -> None: 
        self.name = name 
    
    def __str__(self) -> str:
        return f"{self.name}"

class Card():
    def __init__(self,face:str,suit:str,value:int = None, color:str = None) -> None:
        self.face = face
        self.suit = suit 
        self.value = self.card_value()
        self.color = self.card_color() 
        #self.card_value() 
        #self.card_color()

    def card_value(self) -> int:
        '''assign value to card based on case matching of face card attribute'''
        match self.face:
            case 'J'|'Q'|'K':
                self.value = int(10)
            case 'A':
                self.value = int(11)
            case _:
                self.value = int(self.face)        
        return self.value    

    def card_color(self) -> str:
        '''assign color to card based on case matching of suite card attribute'''
        match self.suit:
            case 'Hearts'|'Diamonds':
                self.color = "Red"
            case _:
                self.color = "Blue"
        return self.color   

    def __str__(self) ->str:
        return f"{ColoredText(f"({self.face},{self.suit},value={self.value})",f"{self.color.lower()}")}"

class Stack():
    def __init__(self) -> None:
        self.stacklist = [] 
        self.stacksum = 0

    def extendstack(self,cards:list[tuple[str,str,int,str]]) -> list[tuple[str,str,int,str]]:
        '''take list of cards to append to stacklist using extend method'''
        return self.stacklist.extend(cards)

    def clearstack(self) -> tuple[list,int]:
        '''clear the stack/list and reset stack's sum to 0 '''
        self.stacklist.clear()
        self.stacksum = 0
        return self.stacklist,self.stacksum

    def sum_cards_in_list(self) -> int:
        '''sum the total values of cards in stack, and return the total value.'''
        self.stacksum: int = sum([card.value for card in self.stacklist])  
        self.subtract_ace_value()
        return self.stacksum
    
    def subtract_ace_value(self) -> int:
        '''if there is an Ace in the stack list and total sum of cards is greater
        than 21, change value of ace from 11 to 1 by subtracting value 10 from sum of cards'''
        sum = self.stacksum
        if self.ace_in_stack() and sum > 21:
            self.stacksum = sum - 10
            return self.stacksum
        else:
            return sum 

    def rmcard_frmstack(self, n: int = 1) -> list[tuple[str,str,int,str]]:     
        '''remove n (argument) number of cards from stack as long as there are n number of cards in deck else raise error'''
        try:
            return [self.stacklist.pop() for count in range(1,n + 1)]            
        except IndexError as err:
            print("no cards left in deck")
            raise
    
    def length_stack(self) -> int:
        return len(self.stacklist)

    def ace_in_stack(self) -> True|False:
        '''return boolean evaluating whether there is an Ace face card in stack'''
        if any(card.face == "A" for card in self.stacklist):
            return True 
    
    def cards_remain(self) -> True|False:
        '''return boolean evaluating whether there remains cards in stack'''
        if len(self.stacklist) > 0:
            return True 
    
    def print_cards(self) -> None:
        '''print each card object in stacklist'''
        for card in self.stacklist:
            print(card)
    
    def __str__(self) -> str: 
        return f"holds: total={self.stacksum}\n {self.stacklist}\n" 

class Deck(Stack):
    ''' Deck is a childclass of Stack inhereting all of Stack class' attributes and methods'''
    def __init__(self):
        super().__init__()
        self.create_deck()
     
    def create_deck(self) -> list[tuple[str,str,int,str]]:
        '''create an intial deck of 52 cards, as a list of card objects. randomize the deck list with shuffle method'''
        self.stacklist.clear()
        face_list: list[str] = [ "A", "J", "Q", "K"] + [str(i) for i in range(2,10+1)]
        suit_list: list[str] = ["Clubs", "Hearts", "Spades", "Diamonds"]
        for face in face_list:
            for suit in suit_list:
                card = Card(face,suit)
                value = card.card_value()
                color = card.card_color()
                self.stacklist.append(Card(face,suit,value,color))     
        random.shuffle(self.stacklist)  
        return self.stacklist

    def multiple_deck(self, n: int = 2) -> list[tuple[str,str,int]]:
        '''create n number of deck objects and return as unified list. default argument of 2'''
        self.stacklist: list[tuple[str,str]] = [self.create_deck() for i in range(1,n + 1)]   
        return self.stacklist
           
    def __str__(self) -> str:
        return f"Cards left in deck: {self.stacklist}"
    
class PlayerHand(Stack):
    '''PlayerHand is child class of Stack inhereting all of Stack's attributes and methods'''
    def __init__(self) -> None:
        super().__init__()
    
    def blackjack(self) -> True|False: 
        '''return true if the stacksum attribute value is 21 and the stack has only 2 cards'''
        if self.stacksum == 21 and self.length_stack() == 2:
            return True 
    
    def bust(self) -> True|False:
        '''return true if stacksum attribute value is greater than 21 '''
        if self.stacksum > 21:
            return True 

    def can_hit(self) -> True|False:
        '''return true if stacksum is less than 21, indicating player can take another card (hit)'''
        if not self.bust():
            return True
        
    def __str__(self) -> str:
        return f"holds total: {self.stacksum}"

class DealerHand(PlayerHand):
    '''DealerHand is a childclass of PlayerHand and shares all same class attributes and methods'''
    def __init__(self):
        super().__init__()
    
class Game():
    def __init__(self,player,wallet,dealer,player_hand,dealer_hand,deck): 
        self.player = player 
        self.wallet = wallet 
        self.dealer = dealer
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.deck = deck

    def greet(self) -> None:
        print(f'''
        {ColoredText(f"{player.name}","light_red")}, welcome to Black Jack the Ripper!!! 
        It's like BlackJack without the complexities of splits,double downs, and other comforts
        that didn't exist during the time of Rippers terror, yet still offers bloody odds..\n 
        ''')

    def rules(self) -> None:
        request_rules = input(ColoredText("Press (y) if you want the game rules, or any other key to proceed: \n", 'green'))
        if request_rules in {"y","Y"}:
            print(ColoredText('''
            Try to beat the dealer's hand without going over the sum of 21. 
            Jack,Queen, and King have a value of 10.
            Face cards (2,3,4...10) have the same value as their corresponding faces.
            Ace has value of 11 unless its inclusion causes your handsum to exceed 21, 
            in which case Ace has value of 1. 

            At the onset of the round, both dealer and player are delt 2 cards. 
            If the sum of the 2 cards is 21, a "black jack" is achieved and the round ends. 
            If player has black jack, while dealer does not, the player wins
            their bet. If both player and dealer have 21, it's called a push (aka a tie) and the player 
            neither wins nor looses their bet. If dealer has blackjack, while player does not, 
            the player looses their bet. When neither player nor dealer has 21 after the first 2 cards 
            are delt, the round continues to optional and/or obligatory hits (additionally delt card(s)). 
            So long as the player has less than that of the dealer, the player must hit.
            Otherwise the player decides if they want to try to increase their total with addition of 
            another card by hitting, or stay at current value. Be forewarned that if the player's hand 
            exceeds 21, the player looses the round and bet. Provided the player does not bust (exceed 21), 
            the dealer must subsequently hit so long as the dealer has less than the player after 
            player stands.Whoever has the greatest number,without exceeding 21, wins the round. 
            A push occurs whenever player and dealer have same value.
            \n''', 'green')) 
        pass

    def game_play(self) -> True|False:
        '''gameplay continued as long as player still has money.'''
        while wallet.have_money():
            return True    

    def start(self) -> None:     
        self.greet()
        self.rules()
        print(str(wallet))
    
    def place_bet(self) -> int:  
        '''take valid user input and return as value of user's bet '''
        while True:
            bet = player.p_input(ColoredText("enter bloody wager ==>: ",'green'))
            try:
                bet = int(bet)
                assert wallet.inrange(bet)
            except ValueError:
              print(ColoredText("only integers accepted\n",'yellow'))
            except AssertionError:
              print(ColoredText("must enter value greater than 0 and not exceeding wallet amount\n",'yellow'))
            else:
                break
        return bet 
      
    def confirm_hit(self) -> None:
        return player.p_input(ColoredText('''
        ==> Ask for another card: (y)\n 
        ==> Stand with current cards: (any key except 'q' or 'y')\n 
        ==> Quit game: (q)\n
        ''', 'green'))    
    
    
## blackjack game logic #####
    def deal(self) -> None: 
        '''take both the player's and dealer's hand stack object instance as arguments, remove 2 card objects from the deck list for both player
        and dealer, and append/extend the cards to each stacklist. Calculate the new hand stack sum for both dealer and player, as well
        as the corresponding card object colors in each stack, by calling respective stack methods. return hand stack, sum. and color lists as tuple'''
        print("...Dealing cards...\n")
        time.sleep(1)
        player_hand.extendstack(deck.rmcard_frmstack(2))
        dealer_hand.extendstack(deck.rmcard_frmstack(2))
        player_hand.sum_cards_in_list()
        dealer_hand.sum_cards_in_list()
        return player_hand.stacklist,player_hand.stacksum,dealer_hand.stacklist,dealer_hand.stacksum

    def hit(self,xhand) -> None:
        xhand.extendstack(deck.rmcard_frmstack())
        xhand.sum_cards_in_list()
        return xhand.stacklist,xhand.stacksum 
        #return player_hand.stacklist,player_hand.stacksum 

    def blackjack_boolist(self) -> list[bool]:
        return [player_hand.blackjack(),dealer_hand.blackjack()]
    
    def eval_blkjk_bool(self):
        bblist = [player_hand.blackjack(),dealer_hand.blackjack()]
        match any(bblist):
            case False:
                return None  
            case True:
                if all(bblist):
                    return 2 
                elif bblist[0]: 
                    return 0
                else:
                    return 1

               
    def opt_hit(self) -> None:
        '''takes user input by calling game's confirm_hit method. if input is y or Y, call game.hit method to add another
        card to player's stacklist'''
        while p:= self.confirm_hit():
            if p in {'y','Y'}:
                self.hit(player_hand)
                self.outmsg()
                if player_hand.bust():
                    break 
            else:
                break

    def standing(self) -> None:
        print(f"** {ColoredText(f"{player.name}",'light_blue')} {ColoredText(f"standing still by post marker",'light_green')} {ColoredText(f"{player_hand.stacksum}",'light_magenta')} **\n")   
        
    def must_hit_plyr(self): 
        '''take either player or dealer stack instance, compare to see if value matches that of dealer or player,
        and assign corresponding player.name and stack.stacksum attributes to n,n2 and xsum,ysum respectively.
        Continue calling game.hit method as long as provided stack instance is less than the other in gameplay and less than 21.
        return new stack'''
        while player_hand.stacksum < dealer_hand.stacksum <= 21:
            print(f"{player.name} has less than {dealer.name}, so must hit for another card.\n")
            print(ColoredText(f"{player.name} says...hit me!...\n","light_cyan"))
            self.hit(player_hand)
            self.outmsg()
            time.sleep(2)
    
    def must_hit_dlr(self):        
        while dealer_hand.stacksum < player_hand.stacksum <= 21:
            print(f"{dealer.name} has less than {player.name}, so must hit for another card.\n")
            print(ColoredText(f"{dealer.name} says...hit me!...\n","light_cyan"))
            self.hit(dealer_hand)
            self.outmsg()
            time.sleep(2)

    def event_bet(self,bet,event_game):
        match event_game: 
            case 0:
                print(f"{ColoredText(f"+{bet} blood drops gained",'red')} ***\n")
                wallet.appnd_run(bet)
            case 1:
                print(f"{ColoredText(f"-{bet} blood drops lost",'red')} ***\n")
                wallet.appnd_run(-1 * bet)
            case 2:
                pass
        return wallet.calc_new_running_balance()
    
    def event_game_round(self):
        if player_hand.stacksum == dealer_hand.stacksum:
            print(f"*** {ColoredText(f"{player.name} blocked the Ripper. neither blood gained,nor lost",'light_red')} ***\n")
            return 2 
        elif player_hand.bust():
            print(f"{ColoredText(f"{player.name}",'light_blue')} {ColoredText("busted and stabbed by the Ripper",'magenta')}")
            return 1 
        elif dealer_hand.bust():
            print(f"*** {ColoredText(f"{player.name} won hand and drew blood from the Ripper.",'light_red')}***\n")
            return 0
        elif player_hand.stacksum > dealer_hand.stacksum:
            print(f"*** {ColoredText(f"{player.name} won hand and drew blood from the Ripper.",'light_red')}")
            return 0
        elif player_hand.blackjack():
            print(ColoredText(f"{player.name} ripped the ripper with a Power Black Jack",'cyan')) 
            return 0
        else: 
            print(f"{ColoredText("dealer won the hand",'magenta')}")
            return 1 
                
    def _pers_hand_dict(self) -> dict:
        return {player.name: player_hand, dealer.name: dealer_hand}
   
    def outmsg(self) -> None: 
        for name,hand_stack in self._pers_hand_dict().items():
        #print(f"{name} {hand_stack}\n {hand_stack.print_cards()}")
            x = f"{name} holds {hand_stack.stacksum} {hand_stack.print_cards()}"
            newx = re.sub("None","",x)
            print(f"{newx}\n")


def main():
    game = Game(player,wallet,dealer,player_hand,dealer_hand,deck)
    #game.greet()
    #game.rules()
    game.start()
    while game.game_play():
        bet = game.place_bet()
        game.deal()
        game.outmsg()
        initial_blk_eval = game.eval_blkjk_bool()
        if initial_blk_eval != None:
            outcome = initial_blk_eval
        else:    
              #if not any(game.blackjack_boolist()):
            game.must_hit_plyr()
            if player_hand.can_hit():
                game.opt_hit()
                if not player_hand.bust():
                    game.standing()
                    game.must_hit_dlr()
    
        outcome = game.event_game_round()
        game.event_bet(bet,outcome)
        #game.outcome(bet)
        print(str(wallet))
        player_hand.clearstack()
        dealer_hand.clearstack()

    print(ColoredText("You have been brutally killed by the Ripper in a dark alley", "light_red"))

if __name__ == "__main__":
    player = Player()
    dealer = Dealer()
    wallet = Money(200)
    player_hand = PlayerHand() 
    dealer_hand = DealerHand()
    deck = Deck()
    main()
