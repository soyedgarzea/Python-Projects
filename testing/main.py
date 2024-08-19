import random


def do_stuff(num: int) -> int | ValueError:  # type: ignore
    try:
        return int(num) + 5
    except ValueError as error:
        return error


def run_guess(guess: int, answer:int):
    if (0 < guess < 11):
        if (guess == answer):
            print("You guessed it!")
            return True
    else:
        print("Guess must be between 1 and 10")

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
