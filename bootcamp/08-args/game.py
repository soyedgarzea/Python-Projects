'''
    _summary_

_extended_summary_
'''
import string
from _art import art


alphabet = list(string.ascii_lowercase)

print(art)


def caesar(original_text, shift_amount, encode_or_decode):
    '''
    encrypt _summary_

    _extended_summary_

    Args:
        original_text (_type_): _description_
        shift_amount (_type_): _description_
    '''
    output_text = ''

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            new_letter_index = alphabet.index(letter) + shift_amount
            new_letter_index %= len(alphabet)
            output_text += alphabet[new_letter_index]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again, Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")
    else:
        should_continue = True
