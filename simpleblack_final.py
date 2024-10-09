#!/usr/bin/python3
import os
import itertools
import random
import time
import termcolor

class ColoredText():
    def __init__(self, text: str, color: str) -> None:
        self.text = text
        self.color = color

    def __str__(self) -> str:
        return termcolor.colored(self.text,self.color)

class Card():
    def __init__(self,face:str,suit:str,value:int = None, color:str = None) -> None:
        self.face = face
        self.suit = suit 
        self.value = self.card_value() 
        self.card_color = self.card_color()

    def card_value(self) -> int:
        if self.face in {'J','Q','K'}:
            self.value = int(10)
        elif self.face == "A":
            self.value = int(11)
        else:
            self.value = int(self.face)        
        return self.value    

    def card_color(self) -> str:
        if self.suit in {'Hearts','Diamonds'}:
            self.color = "Red"
        else: 
            self.color = "Black"
        return self.color   

    def tuplecard(self) -> tuple[str,str,int,str]:
        return tuple([self.face,self.suit,self.value,self.color])

    def __str__(self) ->str:
        return f"({self.face},{self.suit},{self.value},{self.color})"

class Stack():
    def __init__(self) -> None:
        self.stacklist = [] 
        self.stacksum = 0
        self.stackcolor = []

    def appendcard(self, card:tuple[str,str]) -> list:
        '''no card value attribute passed into stacklist'''
        return self.stacklist.append(card)

    def extendstack(self,cards:list[tuple[str,str]]) -> list:
        '''no card value attribute passed into stacklist'''
        return self.stacklist.extend(cards)

    def clearstack(self) -> list:
        return self.stacklist.clear()

    def list_by_cardclass(self) -> list[Card]:
        '''returns list of cards as Card class instances without card value attribute'''
        return [Card(f,s) for f,s in self.stacklist]
    
    def summ_cardss(self) -> int:
        '''populate list of cards from card Class object, sum the total
        values of cards in stack, and return the total value.    '''
        cards: list[Card] = self.list_by_cardclass()
        cardssum: int = sum([card.value for card in cards])  
        '''if there is an Ace in the stack list and total sum of cards is greater
        than 21, change value of ace from 11 to 1 by subtracting value 10 from sum of cards'''
        if self.ace_in_stack() and cardssum > 21:
            cardssum -= 10
        self.stacksum = cardssum
        return self.stacksum
        
    def getcards(self) -> list[tuple[str,str]]:
        return self.stacklist

    def rmcard_frmstack(self, n: int = 1) -> None:     
        try:
            return [self.stacklist.pop() for count in range(1,n + 1)]            
        except IndexError as err:
            print("no cards left in deck")
            raise
    
    def length_stack(self) -> int:
        return len(self.stacklist)

    def ace_in_stack(self) -> True:
        if any(card.face == "A" for card in self.list_by_cardclass()):
            return True 
    
    def colorcards(self) -> list:
        '''populate list of cards in stack by corresponding color value in card class object'''
        self.stackcolor = [card.color for card in self.list_by_cardclass()]
        return self.stackcolor

    def cards_remain(self) -> True:
        if len(self.stacklist) > 0:
            return True 
    
    def stack_as_tuple(self) -> tuple:
        return (self.stacklist,self.stacksum)  
    
    def clearvalue_stack(self) -> int :
        '''reset stack sum value to 0'''
        self.stacksum = 0
        return self.stacksum
    
    def __str__(self) -> str: 
        return f"holds: {self.stacksum}\n {self.stacklist} \n {self.stackcolor}\n" 

class Deck(Stack):
    def __init__(self):
        super().__init__()
        self.create_deck()
    
    def create_deck(self) -> list[tuple[str,str]]:
        '''create deck with face and suite card attrributes only to avoid calculating value for every card.
        randomize list with shuffle method. returns list of tuple objects with face and suite attrributes'''
        
        self.stacklist.clear()
        face_list: list[str] = [ "A", "J", "Q", "K"] + [str(i) for i in range(2,10+1)]
        suit_list: list[str] = ["Clubs", "Hearts", "Spades", "Diamonds"]
        self.stacklist: list[tuple[str,str]] = [cards for cards in list(itertools.product(face_list,suit_list))]
        random.shuffle(self.stacklist)  
        return self.stacklist

    def multiple_deck(self, n: int = 2) -> list[tuple[str,str]]:
        '''create muliple deck objects and return as unified list.'''
        self.stacklist: list[tuple[str,str]] = [self.create_deck() for i in range(1,n + 1)]   
        return self.stacklist
           
    def __str__(self) -> str:
        return f"Cards left in deck: {self.stacklist}"
    
class Player():
    def __init__(self,name: "player") -> None:
        self.name = name 
        self.set_name()
         
    def set_name(self):
        if self.name.lower() != "dealer":
            self.name: str = input("Enter name: ")
        return self.name

    def p_input(self,i: str) -> any:
        '''take and return user/player input. quit program if Q or q entered'''
        _ = input(i)
        if _ in {"Q","q"}:
            exit("Quiting game as you commanded!")
        return _
    
    def __str__(self) -> str:
        return f"{self.name}"

class Money():
    def __init__(self,start:int):
        self.start = start
        self.running = []
        self.__run_start()
       
    def __run_start(self) -> None:
        '''initates a running value for money object, taking number value provided when money object instantiated'''
        self.running.append(self.start)

    def getlast_runningint(self) -> int:
        '''return last value in running money list'''
        return int(self.running[-1])
    
    def have_money(self) -> True:
        if self.running[-1] > 0:
            return True 

    def appnd_run(self,i:int) -> list:
        return self.running.append(i) 
    
    def intrsum_newrun(self) -> list:
        '''take sum of values in running list, reset list to empty, and start new list containing previou sum'''
        itrsum: int = sum(self.running) 
        self.running.clear()
        return self.running.append(itrsum)
        
    def inrange(self,num:int) -> int:
        return num in range(0,max(self.running)+1) 

    def __repr__(self) -> str:
        return f"[{self.start},{self.running}]"

    def __str__(self) -> str:
        return f"!!! You have {ColoredText({self.running[-1]},"light_red")} {ColoredText("blood drops remaining !!!", "red")}\n"

class Game():
    def __init__(self,player: Player, dealer: Player, wallet: Money, player_hand: Stack, dealer_hand: Stack, deck: Deck):
        self.player = player
        self.dealer = dealer
        self.wallet = wallet
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
            If player has the black jack, while dealer does not, the player wins
            their bet. If both player and dealer have 21, it's called a push (aka a tie) and the player 
            neither wins nor looses their bet. If dealer has blackjack, while player does not, 
            the player looses their bet. When neither player nor dealer has 21 after the first 2 cards 
            are delt, the round continues to optional and/or obligatory hits (additionally delt card(s)). 
            So long as the player has less than that of the dealer, the player must hit.
            otherwise the player decides if they want to try to increase their total with addition of 
            another card by hitting, or stay at current value. Be forewarned that if the player's hand 
            exceeds 21, the player looses the round and bet. Provided the player does not bust (exceed 21), 
            the dealer must subsequently hit so long as the dealer has less than the player after 
            player stands.Whoever has the greatest number,without exceeding 21, wins the round. 
            A tie occurs whenever player and dealer have same value.
            \n''', 'green')) 
        pass

    def game_play(self) -> True:
        '''gameplay continued as long as player still has money.'''
        while wallet.have_money():
            return True    
        
    def start(self) -> None:     
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
              print(ColoredText("must enter value within wallet\n",'yellow'))
            else:
                break
        return bet 
      
    def lose(self,bet: int) -> list[int]:
        '''append inverse bet amount (negative) to money list and calculate new money list'''
        print(f"*** {ColoredText(f"{player.name} suffered bood loss",'light_red')} {ColoredText(f"-{bet} drops",'red')} ***\n")
        wallet.appnd_run(-1 * bet)
        return wallet.intrsum_newrun()
    
    def push(self,bet) -> list[int]:
        '''override user inputted bet with value of 0 and calculate new money list'''
        bet: int = 0
        print(f"*** {ColoredText(f"{player.name} blocked the Ripper. neither blood gained,nor lost",'light_red')} ***\n")
        wallet.appnd_run(bet)
        return wallet.intrsum_newrun()
    
    def win(self,bet):
        '''append bet amount to money list and calculate new money list'''
        print(f"*** {ColoredText(f"{player.name} drew blood from the Ripper.",'light_red')}{ColoredText(f"+{bet} blood drops gained",'red')} ***\n")
        wallet.appnd_run(bet)
        return wallet.intrsum_newrun()

    def confirm_hit(self) -> None:
        return player.p_input(ColoredText('''
        ==> Ask for another card: (y)\n 
        ==> Stand with current cards: (any key except 'q' or 'y')\n 
        ==> Quit game: (q)\n
        ''', 'green'))    
    
    ## blackjack game logic #####

    def blackjack(self,handsum: int) -> True:
        '''take integer value of the stacksum attribute, compare to see if value matches that of dealer or player,
        return true if player's stacksum value is 21 with only 2 cards in list'''
        if handsum == player_hand.stacksum:
            hand = player_hand
        elif handsum == dealer_hand.stacksum:
            hand = dealer_hand      
        if handsum == 21 and hand.length_stack() == 2:
            return True
        
    def bust(self,pass_sum: int) -> True:
        '''take integer value of the hand's stacksum attribute, compare to see if value matches that of dealer or player,
        return true if value is greater than 21 '''
        if pass_sum > 21:
            if pass_sum == player_hand.stacksum:
                print(f"{ColoredText(f"{player.name}",'light_blue')} {ColoredText("...stabbed by the Ripper",'magenta')}")
            elif pass_sum == dealer_hand.stacksum:
                print(f"{ColoredText(f"{dealer.name}",'light_blue')} {ColoredText("...stabbed by the Ripper",'magenta')}")
            return True
    
    def hit(self,x: Stack ) -> tuple[list,int]:
        ''' take either the provided player's or dealer's hand stack object instance and append/extend to its list a card drawn from the deck stack. return both new 
        list and its sum. return the new stack list and stacksum value as tuple 
        '''
        return x.extendstack(deck.rmcard_frmstack()), x.summ_cardss()

    def deal(self,y: Stack ,z: Stack):
        '''take both the player's and dealer's hand stack object instance as arguments, remove 2 card objects from the deck list for both player
        and dealer, and append/extend the cards to each stacklist. Calculate the new hand stack sum for both dealer and player, as well
        as the corresponding card object colors in each stack, by calling respective stack methods. return hand stack, sum. and color lists as tuple'''
        build_player_stacks = [x.extendstack(deck.rmcard_frmstack(2)) for x in (y,z)] 
        sum_player_stacks = [x.summ_cardss() for x in (y,z)]
        apply_attr_color_cards = [x.colorcards() for x in (y,z)]
        print("...Dealing cards...\n")
        time.sleep(1)
        return build_player_stacks, sum_player_stacks, apply_attr_color_cards 
 
    def h1_gt_h2(self,pass_sum1: int,pass_sum2: int) -> True:
        '''takes 2 arguments, the stacksum of player and dealer, and returns true if the first stacksum passed is greater than second and less than or
        equal to 21.'''
        if (pass_sum2 < pass_sum1 <= 21):
            return True

    def h1_eq_h2(self,pass_sum1: int =0, pass_sum2: int =0) -> True:
        '''takes two arguments, the stacksum of player and dealer, and evaluates if are the same value. default passed values s et 
        to 0 to avoid need to provide each stacksum in function call'''
        pass_sum1,pass_sum2 = player_hand.stacksum,dealer_hand.stacksum
        if pass_sum1 == pass_sum2:
            return True 

    def h1_lt_h2(self,pass_sum1: int,pass_sum2: int) -> True:
        '''takes 2 arguments, the stacksum of player and dealer, and return true if the 
        first stacksum passed is less than second'''
        if pass_sum1 < pass_sum2:
            return True

    def boolist(self,blist) -> list[bool,bool]:
        '''given a list as an argument, evaluate boolean value of each item in list, and return a list of 
        boolean values'''
        return [bool(x) for x in blist]

    def can_hit(self,xsum) -> True:
        if not self.bust(xsum):
            return True
    
    def opt_hit(self) -> None:
        '''takes user input by calling game's confirm_hit method. if input is y or Y, call game.hit method to add another
        card to player's stacklist'''
        while p:= self.confirm_hit():
            if p in {'y','Y'}:
                self.hit(player_hand)
                self.outmsg()
                if self.bust(player_hand.stacksum):
                    break 
            else:
                break

    def standing(self) -> None:
        print(f"** {ColoredText(f"{player.name}",'light_blue')} {ColoredText(f"standing still by post marker",'light_green')} {ColoredText(f"{player_hand.stacksum}",'light_magenta')} **\n")   
    
    def outcome(self,bet: int) -> None:   
        '''takes argument of the player's bet, assigned during call to game.place_bet method during game play, and performs 
        series of evaluations of expressions to determine if player won, lost, or tied during round play. bet argument passed
        into game.win,game.loose,game.push methods respectively to generate a new total of money object'''
        if self.h1_eq_h2():
            self.push(bet)
        elif self.blackjack(player_hand.stacksum) and not self.blackjack(dealer_hand.stacksum):    
            print(ColoredText(f"{player.name} ripped the ripper with a Power Black Jack",'cyan')) 
            self.win(bet)
        elif self.bust(dealer_hand.stacksum) or self.h1_gt_h2(player_hand.stacksum,dealer_hand.stacksum):
            self.win(bet)
        else:
            print(f"{ColoredText("dealer won the hand",'magenta')}...{ColoredText(f"{player.name} lost a finger..",'light_red')}\n")
            self.lose(bet)
    
    def must_hit(self,xhand: Stack) -> Stack: 
        '''take either player or dealer stack instance, compare to see if value matches that of dealer or player,
        and assign corresponding player.name and stack.stacksum attributes to n,n2 and xsum,ysum respectively.
        Continue calling game.hit method as long as provided stack instance is less than the other in gameplay and less than 21.
        return new stack'''

        if xhand == player_hand:         
            n,n2 = player.name,dealer.name
            xsum,ysum = player_hand.stacksum,dealer_hand.stacksum
            str1 = ColoredText("...hit me!...\n","blue")
        elif xhand == dealer_hand:
            n,n2 = dealer.name,player.name
            xsum,ysum = dealer_hand.stacksum,player_hand.stacksum
            str1 = ColoredText("...dealer...hitting\n","blue")
        
        while (xsum < ysum < 21):
            #while self.h1_lt_h2(xsum,ysum) and self.can_hit(xsum):    
            print(f"{n} has less than {n2}, so must hit for another card.")
            print(f"{str1}\n")
            self.hit(xhand)
            time.sleep(2)
            self.outmsg()
            xsum,ysum = xhand.stacksum,ysum 
        return xhand 

    
    def clear_hands(self, phand: Stack,dhand: Stack) -> list[list,int]:
        '''takes 2 arguments, player and dealer stack instances, and calls stack.clearstack and stack.clearvalue_stack methods
        to set stacklist to emply list with stacksum value of 0'''
        return [(x.clearstack(),x.clearvalue_stack()) for x in (phand,dhand)]

    def _pers_hand_dict(self) -> dict:
        return {player.name: player_hand, dealer.name: dealer_hand}
   
    def outmsg(self) -> None: 
        for x,y in self._pers_hand_dict().items():
            print(f"{x} {y}\n")


def main():
    game = Game(player,dealer,wallet,player_hand,dealer_hand,deck)
    game.greet()
    game.rules()
    game.start()
    while game.game_play():
        bet = game.place_bet()
        game.deal(player_hand,dealer_hand)
        game.outmsg()
        blackj_boolst = game.boolist([game.blackjack(x) for x in (player_hand.stacksum,dealer_hand.stacksum)])
        if not any(blackj_boolst):
            game.must_hit(player_hand)
            if not game.bust(player_hand.stacksum):
                game.opt_hit()
                if not game.bust(player_hand.stacksum):
                    game.standing()
                    game.must_hit(dealer_hand)
                    game.outcome(bet)             
        else:
            game.outcome(bet)
            
        print(str(wallet))
        game.clear_hands(player_hand,dealer_hand)

    print(ColoredText("You have been brutally killed by the Ripper in a dark alley", "light_red"))

if __name__ == "__main__":
    player = Player("p1")
    dealer = Player("dealer")
    wallet = Money(200)
    player_hand = Stack() 
    dealer_hand = Stack()
    deck = Deck()
    main()
