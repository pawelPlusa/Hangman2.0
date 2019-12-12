import time
import os
import sys
import random
from datetime import date
import calendar

def f_dynamic_path_to_initial_list(file_name): 
    """This function allow us to open file with
    the list of cities without regard to location folder """
    dir_path = os.path.dirname(__file__)
    list_file = dir_path+'/'+file_name
    return list_file

def f_get_word_list():
    file = open(f_dynamic_path_to_initial_list("countries-and-capitals.txt"), 'r')
    word_list = file.readlines()
    splitted_word_list = []
    for line in word_list:
        splitted_word_list.append(line.split('|'))
    file.close
    #print(splitted_word_list)
    return splitted_word_list

def f_find_random_pair():
    splitted_word_list = f_get_word_list()
    pair = splitted_word_list[random.randint(0, len(splitted_word_list))]
    return pair

def f_get_capital(pair):
    """gets a pair of country and city and returns only city"""
    temp = pair
    capital = str.strip(temp[1]).upper()
    return capital

def f_get_country(pair):
    """gets a pair of country and city and returns only contry"""
    temp = pair
    country = str.strip(temp[0]).upper()
    return country

def f_mask_word(word):
    masked_rand_word = [' ' if i == " " else "_" for i in list(word)]
    return masked_rand_word

def f_prepare_initial_board():
    pair = f_find_random_pair()
    word = f_get_capital(pair)
    country = f_get_country(pair)
    board = f_mask_word(word)
    return country, word, board

def f_print_actual_board(board, used_letters, lives):
    """parameters: board, used letters, lives"""
    print('\nThe word to guess is: ' ,*board, sep= ' ')
    print('Used letters: ', used_letters)
    print('Remaining lives: ' , lives)
    # print('The word to guess is: ',word)
    return word, board

def f_start_game():
    start = input("\nPress '1' to start the game: ")
    while start not in {"1"}:
        start = input("To start, press 1: ")
    return start 

def f_choice_word_or_letter():
    decission = input("\nDecide what to guess: (W)ord or (L)etter ").upper()
    while decission not in {"W", "L"}:
        decission = input("You can only press W or L. ").upper()
    return decission    

def f_guess_letter(word):
    global lives
    global board
    global complete
    global sleep
    global used_letters
    
    guessed_letter = input("Please type desired letter: ").upper()
    while guessed_letter in used_letters:
        guessed_letter = input("Letter already used. Please type a different letter: ").upper()
        
    used_letters.append(guessed_letter)
    index = 0
    success = 0
    for i in list(word):
        if i == guessed_letter:
            board[index] = guessed_letter
            success += 1 
            print("\nThat's a correct guess!")
        index += 1
            
    if success == 0:
        print("\nWrong guess, you lost 1 live")
        while lives > 0:
            print(hangman_drawings[7-lives])
            break
        lives -= 1
    if list(word) == board:
        print("n/Yay! You won't be hanged today! ")
        complete = 1
    if lives == 0:
        f_final_countdown()
        print('The secret word was: ', word)

def f_guess_word(word):
    global lives
    global complete
    guessed_word = input("\nPlease provide the word: ").upper()
    if word == guessed_word:
        print("Success!")
        complete = 1
    else:
        lives -= 2
        print("Wrong guess, you lost 2 lives.")
        if lives > 0:
            print(hangman_drawings[7-lives])
        if lives <= 0:
            print(hangman_drawings[6])
            f_final_countdown()
            print('The secret word was: ', word)

def f_final_countdown():
    print("3..")
    time.sleep(0.5)
    print('2..')
    time.sleep(0.5)
    print('1...')
    time.sleep(0.5)
    print('YOU ARE DEAD')

def f_repeat():
    if lives <= 0 or complete == 1:
        rep = input('Want to play again? YES - press Y, NO - press any other key! ').upper()
        if rep == "Y":
            return 1
        else:
            return 0

def f_give_a_clue(country,lives):
    """paramters: country, lives. Gives a clue when lives <=3"""
    current_day=calendar.day_name[date.today().weekday()]
    
    if lives <= 3:
        print(f"As we want hang you today, as this is {current_day}, so you can have a clue if you type \"Y\".")
        ans=input(f"So what is your decission? ").upper()
        if ans == "Y":
            if_was_clue = 1
            print(f"So this is the clue - the city you are looking for is the capital of {country}")
            return if_was_clue
    # else:
    #     print("You still don't deserve a clue")

def f_reset_main_counters():
    global complete 
    global decission
    global lives
    global used_letters
    global board
    complete = 0
    decission = 0
    lives = 7
    used_letters = []
    board = []

def f_main():
    global word
    global lives
    global complete
    global board #needed to be set here otherwise if game was repeated f_guess word was giving board with guessed earlier signs, should be again covered
    global used_letters #same reason as with board line above
    again = 1
    clue = 0

    while again == 1:
        f_reset_main_counters()
        f_start_game()
        country,word,board = f_prepare_initial_board()
        while (complete == 0) and (lives > 0):
            f_print_actual_board(board, used_letters, lives)
            if clue != 1:
                clue = f_give_a_clue(country, lives)
            decission = f_choice_word_or_letter()
            if decission == 'W':
                f_guess_word(word)
                again = f_repeat()
            else:
                f_guess_letter(word)
                again = f_repeat()

word = ''

lives = 7
used_letters = []

complete = 0
decission = 0
board = []
hangman_drawings = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

f_main()
