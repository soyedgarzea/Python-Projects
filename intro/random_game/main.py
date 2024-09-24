import random


def guess_number():
    random_number = random.randint(0, 10)
    user_guess = input('Which number between 0 and 10 am I thinking? ')

    try:
        user_guess = int(user_guess)

        if 0 < user_guess < 11:
            if user_guess == random_number:
                print('You got it!')
            else:
                print(f'You got it wrong. I was thinking in {random_number}')
                guess_number()
        else:
            print('Try another number')
            guess_number()
    except ValueError:
        print('Try with a number')
    guess_number()


guess_number()
