"""A game called Hangman"""

from random import randint
from game import Game #imports all of the classes within the module in this case just Game class
instance = Game()

#lets create a dictionary with our words from words.txt
dict_of_words = {}
dict_key = 0
with open('\\Users\\Lenovo\\Desktop\\GitHUB\\Hangman\\words.txt') as file_object:
    for line in file_object:
        dict_key += 1
        dict_of_words[dict_key] = line.strip()


instance.initialize_word(dict_of_words[randint(1, 1)])
print(instance.word)
instance.initialize_guess_word()


print("Hello and Welcome to 'Hangman'")
print("'Hangman' is best experienced in 'Full Screen' mode")
print(instance.guess)



instance.current_letter = input("Please enter an alphabetical charater you suspect is present in the mystery word:")
instance.update_guess()
if instance.correct_letter:
    print("\nCongratulations, this letter is present")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)
    


instance.current_letter = input("Please enter an alphabetical charater that you suspect is present in the word:")
instance.update_guess()
if instance.correct_letter:
    print("Congratulations, that is a correct letter")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)


instance.current_letter = input("Please enter an alphabetical charater that you suspect is present in the word:")
instance.update_guess()
if instance.correct_letter:
    print("Congratulations, that is a correct letter")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)

instance.current_letter = input("Please enter an alphabetical charater that you suspect is present in the word:")
instance.update_guess()
if instance.correct_letter:
    print("Congratulations, that is a correct letter")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)


instance.current_letter = input("Please enter an alphabetical charater that you suspect is present in the word:")
instance.update_guess()
if instance.correct_letter:
    print("Congratulations, that is a correct letter")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)

instance.current_letter = input("Please enter an alphabetical charater that you suspect is present in the word:")
instance.update_guess()
if instance.correct_letter:
    print("Congratulations, that is a correct letter")
    print(instance.guess)
else:
    with open('text_images\\1.txt') as file_object:    
        contents = file_object.read()
    print(contents)
    print(instance.guess)


