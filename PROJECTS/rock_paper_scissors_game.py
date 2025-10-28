import random

ROCK='r'
SCISSORS='s'
PAPER='p'
emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice!")
            continue   

def display_choice(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determining_winner(user_choice, computer_choice):
    while True:   
        if user_choice == computer_choice:
            print("It's a tie!")
        elif ((user_choice == ROCK and computer_choice == SCISSORS) or
              (user_choice == PAPER and computer_choice == ROCK) or
              (user_choice == SCISSORS and computer_choice == PAPER)):
            print('You win!')
        else:
            print('Computer wins!')
            print('You lose!')
        break        
        
def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        determining_winner(user_choice, computer_choice)
        should_continue = input('Play again? (y/n): ').lower()
        if should_continue == 'n':
            break
play_game()    
    