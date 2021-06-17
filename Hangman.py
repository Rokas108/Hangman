"""A game called Hangman"""

from random import randint
from game import Game #imports Game class
image_filepaths = (
    'text_images\\1.txt', 'text_images\\2.txt', 'text_images\\3.txt', 'text_images\\4.txt', 
    'text_images\\5.txt', 'text_images\\6.txt', 'text_images\\7.txt', 'text_images\\8.txt'
    )

#lets create a dictionary with our words from words.txt
dict_of_words = {}
dict_key = 0
players_answer = "Y"
with open('.\\words.txt') as file_object:
    for line in file_object:
        dict_key += 1
        dict_of_words[dict_key] = line.strip()


print("\nHello and Welcome to 'Hangman'")
print("\n'Hangman' is best experienced in 'Full Screen' mode")

intends_to_play = True
while intends_to_play is True:
    #Let an instance of the game begin
    hang_index = 0
    try:
        instance = Game()
        instance.reset_game()
        random_key = randint(1, 49)
        instance.initialize_word(dict_of_words[random_key])
        instance.initialize_guess_word()
        while hang_index != 8 and instance.game_won != True:
            instance.current_letter = input("\nPlease enter an alphabetical charater you suspect is present in the mystery word:")
            if instance.game_won == False:
                if instance.current_letter.isalpha():
                    instance.update_guess()
                    instance.check_if_game_won()
                    if instance.correct_letter:
                        print("\nCongratulations, this letter is present")
                        print("\n" + " ".join(instance.guess))
                    else:
                        with open(image_filepaths[hang_index]) as file_object:    
                            contents = file_object.read()
                        print(contents)
                        print(" ".join(instance.guess))
                        hang_index += 1
                    instance.check_if_game_won()
                    if instance.game_won == True:
                        print("You have won the game. Praise be!\n")
                        players_answer = input("If you would fancy another one of em' games, please enter Y, otherwise GG and Farewell:")
                    if (hang_index - 1) == 7:
                        print("You have been hanged\n")
                        players_answer = input("If you would fancy another one of em' games, please enter Y, otherwise GG and Farewell:")
                else:
                    print("\nThe character is missing from the alphabet")
    except:
        pass
    if  players_answer != "Y" and players_answer != "y":
        intends_to_play = False
            
