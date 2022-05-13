from game.card import Card
import random

class Dealer:
    """A dealer of the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
    
        is_playing (boolean): Whether or not the game is being played.
        card (Card): An instance of a Card
        first_card (int): holder of the value of the first drawn Card
        second_card (int): holder of the value of the second drawn Card
        points (int): The current points of the player.
        guess (str): The guess of the player higher (h) or lower (l)
        risk (int): The starting number 0 that will determine how many points will be increased or deceased depending on the player's input
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
        
            
        draw = self.validateInput("Play again? [y/n]: ", "yn")
        print("")
        
        self.is_playing = (draw == "y")

    def do_updates(self):
        """Show the second card and updates the player's points.

        Args:
            self (Dealer): An instance of Dealer.
        """
        
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
        '''Prompt the player to wager points for their answer and returns a valid number value based on the logic below. 
        
        Attributes:
        The points are determined by player's input
        Minimum bet is always 75 points (even if player's point total is less than 75).
        Maximum bet is always the total number of the player's points at that round.
        
        
        Behaviors:
        Returns at least a minimum of 75 points
        Returns no more than maximum points the player has.
        Returns player's input for points to bet to the bet method.
        
        Args:
            Self (Dealer): An instance of Dealer
            minimum_bet: (int) 75 
            max_bet: (int) Dealer.points
            risk: (int) updates self.risk
            
        '''
        
        
        
        print('Your current point total is ', self.points)
        minimum_bet = 75
        max_bet = self.points
        self.risk = int(self.validateInput('How many points would you like to risk? ', '0123456789'))
        
        if self.risk >= minimum_bet:
            
            if self.risk > self.points:
                print(f'You must be very confident because you exceeded the amount you wager!')
                print(f'Here, your wager will be {max_bet}')
                self.risk = self.points
                return self.risk
                
            else: 
                print(f'Your wager is acceptable.  You wager... {self.risk}')
                return self.risk
        
        
        else:
            self.risk <= minimum_bet
            if self.points <= minimum_bet:
                print('It looks like you are on your last points.')
                print('Here, we will bump your wager up to 75.  Good Luck!!!')
                self.risk = 75
                return self.risk
            
            else:
                print('Dont be afraid to dream big.  Here lets bump your wager up to 75')
                self.risk = 75
                return self.risk
            
        
        
        
        
        
        
        
        
    
    def bet(self):
        ''' Takes player's wager and if applicable will multiply it.  Returns points to be calcualted into total player score
        
        Behaviors:
        Receives wagered points 
        Multiplies wagered points
        Returns the result of wagered points that are multiplied.
        
        
        Args:
        bet: (int) Value receieved from gamble method
        bonus: (int) Value receieved from chance method
        '''
        
        bet = self.risk
        bonus =  self.chance()
        return bet * bonus
       
        
    def chance(self):
        '''Controls the probablity of the point multiplier
        
        Atributes:
        Contains the logic for point multiplier 
        Probablity of activation of multiplier is 30%
        
        Behaviors:
        A randome number will be pulled each round between 1-10.
        If the random number pulled is 3, 6 or, 9 then it will activate a 2x multiplier (activated) otherwise it will return a 1X Multiplier (miss)
        Returns results of the multiplier.
        
        Args:
        multiply: (int) 0
        random_chance: (int) Random number between 1-10
        
         '''
        
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
        """Displays the cards and the points. Also asks the player if they want to play again.
           Checks to see if points lesser than or equal to 0 or if points are greater than or equal to 5000, or if none the game will end 

        Args:
            self (Dealer): An instance of Dealer.
            
        """
        print(f"Next card was: {self.second_card}")
        print(f"Your score is: {self.points}")

        if self.points <= 0:
            print('you lose...')
            self.is_playing = False
            
        elif self.points >= 5000:
            print('YOU WIN !!!')
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