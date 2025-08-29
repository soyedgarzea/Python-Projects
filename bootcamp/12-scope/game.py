'''
    _summary_

_extended_summary_
'''
import random
from art import art

keep_gaming = True

print(art)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = random.choice(range(1, 100))

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

hints_amount = 10

if game_level == 'hard':
    hints_amount = 5


while keep_gaming:

    print(f"You have {hints_amount} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    if hints_amount > 1:
        if guess > number_to_guess:
            print("")
            print("Too high")
            print("")
            hints_amount -= 1
        elif guess < number_to_guess:
            print("")
            print("Too low")
            print("")
            hints_amount -= 1
        else:
            keep_gaming = False
            print("")
            print("You have guessed 👏")
            print("")
    else:
        keep_gaming = False
        print("")
        print("You have not guessed 😞")
        print(f"The number was {number_to_guess}")
        print("")
