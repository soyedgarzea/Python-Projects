from random import choice

options = {
    'r': '🪨',
    'p': '🧻',
    's': '🔪'
}

score = [0, 0]


def init_game():
    user_option = input('''
What do you choose?
Rock = R
Paper = P
Scissors = S\n''').lower()
    computer_option = choice(list(options.keys()))

    print(f'You have selected: {options[user_option]}')
    print(f'Computer has selected: {options[computer_option]}')

    game_logic(user_option, computer_option)


def game_logic(user, computer):
    if user == computer:
        print('It is a draw')

    if user == 'r':
        if computer == 's':
            score[0] += 1
            print('Rock smashes scissors! You win!')
        elif computer == 'p':
            score[1] += 1
            print('Rock crushes paper! Computer wins!')
    elif user == 's':
        if computer == 'p':
            score[0] += 1
            print('Scissors cuts paper! You win!')
        elif computer == 'r':
            score[1] += 1
            print('Scissors are no match for rock! Computer wins!')
    elif user == 'p':
        if computer == 'r':
            score[0] += 1
            print('Paper covers rock! You win!')
        elif user == 'p' and computer == 's':
            score[1] += 1
            print('Paper is no match for scissors! Computer wins!')

    play_again()


def play_again():
    again = input('Do you want to play again? Y / N ').lower()

    if again == 'y':
        init_game()
    elif again == 'n':
        print(f'''Thanks for playing! The final score is You:{
              score[0]} wins / Computer:{score[1]} wins''')


init_game()
