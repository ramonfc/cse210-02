import random

class Card:
    """A card deck from 1 to 13. 
    
    The responsibility of the card is to give a random card from 1 to 13.

    Attributes:
        value (int): The value of the card.
    """
    def __init__(self):
        """Constructs a new instance of Card and has an attribute value.

        Args:
            self (Player): An instance of Player.
        """
        self.value = 0
    
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)
    

