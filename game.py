"""A class that defines an instance of a game"""

class Game:
    """an instance in this class represents a single game"""

    def __init__(self):
        """Initialize attributes to describe a game."""
        self.word = []
        self.guess = []
        self.current_letter = ""
        self.correct_letter = True

        self.odometer_reading = 0
        
    def initialize_word(self, word):
        for letter in word:
            self.word.append(letter)

    def initialize_guess_word(self):
        """Create a quess based on the game's word"""
        for letter in self.word:
            self.guess.append("_")

    def update_guess(self):
        """For every letter in game's word that is the same as current letter, reveal that letter"""
        index = 0
        self.correct_letter = False
        for letter in self.word:
            if letter.lower() == self.current_letter.lower():
                self.guess[index] = letter.upper()
                self.correct_letter = True
            index +=1