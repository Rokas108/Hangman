"""A game called Hangman"""

from random import randint
from game import Game #imports all of the classes within the module in this case just Game class
dict_of_words = {}
index = 0

with open('words.txt') as file_object:
    for line in file_object:
    index += 1
    dict_of_words[index] = line.strip()

print(dict_of_words)

self.game_word = split(our_dictionary[randint(1, 50)])




print("Hello and Welcome, to the game 'Hangman'")



