import os
from random import randint

class Money():
    def __init__(self,start):
        self.start = start
        self.running = []
        self.__run_start()
       
    def __run_start(self):
        self.running.append(self.start)

    def getlast_runningint(self):
        return int(self.running[-1])
    
    def have_money(self):
        if self.running[-1] > 0:
            return True 

    def appnd_run(self,i):
        return self.running.append(i) 
    
    def intrsum_newrun(self):
        itrsum = sum(self.running) 
        self.running.clear()
        return self.running.append(itrsum)
        
    def inrange(self,num):
        return num in range(0,max(self.running)+1) 

    def __repr__(self):
        return f"[{self.start},{self.running}]"

    def __str__(self):
        return f"Your Wallet stolen from Vox far-right party contains ${self.running[-1]}\n"

class Dedos():
    def __init__(self):
        self.dielist = []
        self.get_dicelist()
    
    def get_dicelist(self):
        self.dielist.clear()
        x,y, = randint(1,6),randint(1,6)
        for i in [x,y, x + y ]: 
            self.dielist.append(i)
    
    def reset_dice(self):
        self.dielist.clear()
    
    def get_dietotal(self):
        return int(self.dielist[-1])
    
    def roll(self):
        self.dielist.clear()
        self.get_dicelist()
        print(str(dedos))
        return self.get_dietotal()

    def __str__(self):
        return f"you rolled a {self.dielist[-1]}: {self.dielist[0]},{self.dielist[1]}"
    
    def __repr__(self):
        return f"{self.dielist}"

class Player():
    def __init__(self,name = "player"):
        self.name = name 
        self.set_name()
         
    def set_name(self):
        self.name = input("Enter name: ")
    
    def p_input(self,i):
        _ = input(i)
        if _ in {"Q","q"}:
            exit("Quiting game as you commanded!")
        return _
    
    def __str__(self):
        return f"{self.name}"

class Game():
    def __init__(self, money, dedos, player):
        self.money = money
        self.dedos = dedos
        self.player = player 

    def greet(self):
        print(f'''
        Welcome {player.name} to Catalan Craps!!! 
        It's the same as craps, but your chance
        of winning is much less than normal.
        Just like the Catalan independence movement  
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
    
    def throwprmpt(self):
        return player.p_input("press any key to roll or (q) to quit:  ##\n")
    
    def win(self,bet):     
        print("win")
        return wallet.appnd_run(bet)
      
    def lose(self,bet):
        print("lose")
        return wallet.appnd_run(-1 * bet)

wallet = Money(200)
dedos = Dedos()
player = Player("p1")
game = Game(wallet,dedos,player)

game.greet()
game.rules()
game.start()
while game.game_play():    
    bet = game.place_bet()
    game.throwprmpt()
    comeout = dedos.roll()
    if comeout in {7,11}:
        game.win(bet)
    elif comeout in {2,3,12}:
        game.lose(bet)
    else:
         proll = 0 
         while proll not in {7,11,comeout}:
             game.throwprmpt()
             proll = dedos.roll()
         if proll == comeout:
             game.win(bet)
         elif proll in {7,11}:
             game.lose(bet)

    wallet.intrsum_newrun()
    print(str(wallet))
    #dedos.reset_dice()             
print("You are broke as fuck, just like the Catalan Independence Movement. Back to Madrid!")

