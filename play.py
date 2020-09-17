6# Write your code here

import random


computer_choice = random.choice(['rock','paper','scissors'])


win = {
    'rock':'scissors',
    'scissors':'paper',
    'paper':'rock'
    }

def play(user, comp_choice):

    if user == comp_choice:

        print(f"There is a draw ({comp_choice})")
    elif win[user] == comp_choice:
        pass
    elif win[user] == comp_choice:

        print(f'Sorry, but the computer chose {comp_choice}')

while True:
    wish = input("")
    play('rock', computer_choice)
    if wish == 'rock' or wish == 'paper' or wish == 'scissors':
        play(wish, computer_choice)
    elif wish == '!exit':
        print("Bye!")
        break

