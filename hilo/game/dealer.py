from game.card import Card

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
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
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
        self.guess = input("Higher or lower? [h/l]: ")
    
    def get_play_again(self):
        """Ask the player if they want to play again.

        Args:
            self (Dealer): An instance of Dealer.
        """
        draw = input("Play again? [y/n]: ")
        print("")
        self.is_playing = (draw == "y")

    def do_updates(self):
        """Show the second card and updates the player's points.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return 
        
        if self.first_card > self.second_card:
            correc_answer = "l"
        else:
            correc_answer = "h"
            
        if correc_answer == self.guess:
            self.points += 100
        else: self.points -= 75

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

        self.get_play_again()