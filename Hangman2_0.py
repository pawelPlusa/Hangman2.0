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

# def f_input_list_separation(word_list):
#     #my_word_list_len = []
#     for line in word_list:
#         my_word_list.append(line.split('|'))
#         #my_word_list_len = len(my_word_list)


def f_random_word():
    #global word
    #my_word_list_len = []
    file = open(f_dynamic_path_to_initial_list("countries-and-capitals.txt"), 'r')
    word_list = file.readlines()
    my_word_list = []
    for line in word_list:
        my_word_list.append(line.split('|'))
        #my_word_list_len = len(my_word_list)
    word = (my_word_list[random.randint(1, len(my_word_list))][1].upper())
    file.close
    return word

def f_mask_word(word):
    masked_rand_word = ['_' for i in range(len(list(word)))]
    return masked_rand_word

def f_start_game():
    global again 
    global complete 
    global decission
    global lives
    global word
    global board
    global used_letters
    again = 1
    complete = 0
    decission = 0
    lives = 6

    start = input("\nPress '1' to start the game: ")
    while True:
        if start == '1':
            word = str.strip(f_random_word())
            board = f_mask_word(word) #this resetts board - not really by PP
            used_letters = [] #this resetts used letters - not really by PP
            print(word)
            print('\nThe word to guess is: ' ,board)
            # print('Used letters: ', used_letters)
            # print('Remaining lives: ' , lives)
            break
        else:
            start = input("To start, press 1: ")

def f_choice_word_or_letter():
    decission = input("\nDecide what to guess: (W)ord or (L)etter ").upper()
    # print(decission)
    while True:
        if decission == "W":
            #print(decission)
            return decission
        elif decission == "L":
            decission = decission.upper()
            #print(decission)
            return decission
        else:
            decission = input("You need to press W or L only ").upper()
            return decission

def f_guess_letter(word):
    global lives
    global board
    global complete
    global sleep
    # global used_letters
    print('\nThe word to guess: ' ,board)
    print('Remaining lives: ' , lives)
    print('Used letters: ', used_letters)
    guessed_letter = input("Please type desired letter ").upper()
    used_letters.append(guessed_letter)
    index = 0
    success = 0
    for i in list(word):
        if i == guessed_letter:
            board[index] = guessed_letter
            success += 1
        index += 1
    print("\nThat's a correct guess!")
    if success == 0:
        print("\nWrong guess, you lost 1 live")
        lives -= 1
        print('Remaining lives: ' , lives, '\n')
    if list(word) == board:
        print("n/Yay! You won't be hanged today! ")
        complete = 1
    print('The word to guess: ' ,board)     
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
        rep = input('Wanna play again? If YES - press Y, if NO press any other key! ').upper()
        if rep == "Y":
            return 1
        else:
            return 0

def f_main():
    global word
    global lives
    global complete
    global board #needed to be set here otherwise if game was repeated f_guess word was giving board with guessed earlier signs, should be again covered
    global used_letters #same reason as with board line above
    again = 1
    # board = f_mask_word(word)
    while again == 1:
        f_start_game()
        # system('clear')
        while (complete == 0) and (lives > 0):
            print('Remaining lives: ' , lives)
            dec = f_choice_word_or_letter()
            # print(dec)
            if dec == 'W':
                f_guess_word(word)
                again = f_repeat()
            else:
                f_guess_letter(word)
                again = f_repeat()

#word = ''
word = ''

#word = 'sopot'.upper()


lives = 6
used_letters = []


complete = 0
decission = 0
#board = f_mask_word(word)
board = []
f_main()
