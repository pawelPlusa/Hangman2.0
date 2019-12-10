import time
import os
import sys
import random

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
    return splitted_word_list

def f_random_word():
    splitted_word_list = f_get_word_list()
    word = str.strip((splitted_word_list[random.randint(1, len(splitted_word_list))][1].upper()))
    #word = str.strip(word)
    return word

def f_mask_word(word):
    masked_rand_word = [ '_' for i in range(len(list(word)))]
    return masked_rand_word

def f_prepare_initial_board():
    word = f_random_word()
    board = f_mask_word(word)
    # print('\nThe word to guess is: ' ,word,board)
    return word, board

def f_print_actual_board(board, used_letters, lives):
    word = f_random_word()
    board = f_mask_word(word)
    """parameters: board, used letters, lives"""
    print('\nThe word to guess is: ' ,board)
    print('Used letters: ', used_letters)
    print('Remaining lives: ' , lives)
    return word, board

#print(f_prepare_initial_board())
#w,b = f_prepare_initial_board()


def f_start_game():
    # global again 
    # global complete 
    # global decission
    # global lives
    # global word
    # global board
    # global used_letters
    # again = 1
    # complete = 0
    # decission = 0
    # lives = 6

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
    # print('\nThe word to guess: ' ,board)
    # print('Remaining lives: ' , lives)
    # print('Used letters: ', used_letters)
    guessed_letter = input("Please type desired letter ").upper()
    used_letters.append(guessed_letter)
    index = 0
    success = 0
    for i in list(word):
        if i == guessed_letter:
            board[index] = guessed_letter
            print("\nThat's a correct guess!")
            success += 1
        index += 1
    if success == 0:
        print("\nWrong guess, you lost 1 live")
        lives -= 1
        # print('Remaining lives: ' , lives)
    if list(word) == board:
        print("n/Yay! You won't be hanged today! ")
        complete = 1
    # print('The word to guess: ' ,board)     
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
        if lives <= 0:
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

def f_reset_main_counters():
    global complete 
    global decission
    global lives
    global used_letters
    global board
    complete = 0
    decission = 0
    lives = 6
    used_letters = []
    board = []

def f_main():
    global word
    global lives
    global complete
    global board #needed to be set here otherwise if game was repeated f_guess word was giving board with guessed earlier signs, should be again covered
    global used_letters #same reason as with board line above
    again = 1
    # board = f_mask_word(word)
    while again == 1:
        f_reset_main_counters()
        f_start_game()
        word,board = f_prepare_initial_board()
        #f_print_actual_board(board, used_letters, lives)
        # system('clear')
        while (complete == 0) and (lives > 0):
            #print('Remaining lives: ' , lives)
            f_print_actual_board(board, used_letters, lives)
            decission = f_choice_word_or_letter()
            if decission == 'W':
                f_guess_word(word)
                again = f_repeat()
            else:
                f_guess_letter(word)
                again = f_repeat()

word = ''

lives = 6
used_letters = []

complete = 0
decission = 0
board = []
f_main()
