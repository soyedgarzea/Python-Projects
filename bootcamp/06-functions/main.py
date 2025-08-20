'''
    _summary_

_extended_summary_
'''
from random import choice
from hangman_words import word_list
from hangman_asci import stages, logo

lives = 6

print(logo)

chosen_word = choice(word_list)
# print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

# word_length = len(chosen_word)
# for letter in range(word_length):
#     placeholder += "_"

print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    print(f"********** {lives}/6 LIVES LEFT **********")
    guess = input('Guess a letter: ').lower()

    if guess in correct_letters:
        print(f"You've already guesses {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print('********** GAME OVER "**********')
            print(f'********** IT WAS {chosen_word} "**********')

    if "_" not in display:
        game_over = True
        print("********** YOU WIN **********")

    print(stages[lives])
