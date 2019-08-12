"""A class that defines an instance of a game"""

class Game:
    """an instance in this class represents a single game and it's attributes"""

    def __init__(self):
        """Initialize attributes to describe a game."""
        self.word = []
        self.guess = []
        self.current_letter = ""
        self.correct_letter = False
        self.game_won = False
        
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
                self.guess[index] = letter
                self.correct_letter = True
            index +=1
    
    def check_if_game_won(self):
        """checks whether the current game has been won"""
        if self.word == self.guess:
            self.game_won = True
        else:
            self.game_won = False
    
    def reset_game(self):
        """prepares itself for a new game"""
        self.word = []
        self.guess = []
        self.current_letter = ""
        self.correct_letter = False
        self.game_won = False