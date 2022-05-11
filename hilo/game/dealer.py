from game.card import Card
import random

class Dealer:
    """A dealer of the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        card (Card): An instance of a Card
        first_card (int): holder of the value of the first drawn Card
        seconrd_card (int): holder of the value of the second drawn Card
        points (int): The current points of the player.
        guess (str): The guess of the player higher (h) or lower (l)
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = True
        self.card = Card()
        self.first_card = 0
        self.second_card = 0
        self.points = 300
        self.guess = ""
        self.risk = 0
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        
            
        while self.is_playing:
            
            self.gamble() 
            self.get_guess()
            self.do_updates()
            self.do_outputs()
    
    def get_guess(self):
        """Draw the cards and show the first card, then ask if the second is higher or lower.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.first_card == 0:
            self.card.draw()
            self.first_card = self.card.value
        else:
            self.first_card = self.second_card
        self.card.draw()
        self.second_card = self.card.value
        print(f"The card is {self.first_card}")
        self.guess = self.validateInput("Higher or lower? [h/l]: ", "hl") 
    
    def get_play_again(self):
        """Ask the player if they want to play again.

        Args:
            self (Dealer): An instance of Dealer.
        """
        # if self.points <= 0:
        #     self.is_playing = False
            
        print(self.points)
            
        draw = self.validateInput("Play again? [y/n]: ", "yn")
        print("")
        
        self.is_playing = (draw == "y")

    def do_updates(self):
        """Show the second card and updates the player's points.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return exit() 
        
        if self.first_card > self.second_card:
            correc_answer = "l"
        else:
            correc_answer = "h"
            
        
            
        if correc_answer == self.guess:
            self.points += self.bet()
            print('you guessed it correct')
        else: 
            self.points -= self.bet()
            print('you guessed incorrectly')
            
            
        
            
            
        
    def gamble(self):
        '''This will prompt the player to wager points for their answer.'''
        self.risk = int(input('How many points would you like to risk? '))
        
    
    def bet(self):
        ''' The minimum wager is 75 points and the maximum wager is the player total points.
        If the player incorrectly inputs then it will automatically be at least 105 points that will be wagered then multiplied by the multiplyer if it applies.'''
        
        bet = 0
        minimum_bet = 0
        bonus =  self.chance()
        
        if self.risk >= minimum_bet:
            
            if self.risk > self.points:
                print(f'You must be very confident because you exceeded the amount you wager!  Here, your wager will be {self.points}')
                bet = self.points * bonus
                return bet
                
            else:
                bet = self.risk * bonus
                print(f'Your wager is acceptable.  You wager... {bet}')
                return bet
                
        else:
            bet += minimum_bet * bonus
            return bet    
        
    def chance(self):
        '''This will determine by random if the player will get a bonus multiplier to increase the potential points earned or lost. 
        How this is determined is a random number between 1 and 10.  Current probablity for multiplier to active is 30% '''
        
        multiply = 0
        random_chance = random.randint(1,10)
        if random_chance == 3 or random_chance == 6 or random_chance == 9:
            print('It is you lucky day!  You get a 2x MULTIPLIER!!!')
            multiply = 2
            return multiply
            
        else:
            multiply = 1
            return multiply
    
        
        
        

    def do_outputs(self):
        """Displays the dice and the points. Also asks the player if they want to roll again.
           Also check if there were 1 or 5, if none the game will end 

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"Next card was: {self.second_card}")
        print(f"Your score is: {self.points}")

        if self.points <= 0:
            self.is_playing = False
            

        else:
            self.get_play_again()


    def validateInput(self, message, expected_values):
        """Validate if the user input is an expected input

        Args: 
        self (Dealer): An instance of Dealer.
        message (str): message to ask to the user
        expected_values (str): possible right options
        
        """

        user_input = input(message)
        repeat = True
        while repeat == True:
            if user_input in expected_values:   
                guess = user_input
                repeat = False
            else:
                print("Bad input. Try again")
                user_input = input(message)
                repeat = True
                
        return guess