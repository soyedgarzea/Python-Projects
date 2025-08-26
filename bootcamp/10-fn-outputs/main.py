'''
    _summary_

_extended_summary_
'''
from art import art


def add(a, b):
    '''
    add _summary_

    _extended_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return a + b


def subtract(a, b):
    '''
    subtract _summary_

    _extended_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return a - b


def multiply(a, b):
    '''
    multiply _summary_

    _extended_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return a * b


def divide(a, b):
    '''
    divide _summary_

    _extended_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    '''
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def get_number(target):
    return float(input(f'What is the {target} number? '))


def calculate():
    print(art)
    num1 = get_number('first')
    keep_operating = True

    while keep_operating:

        for symbol in operations:
            print(symbol)

        operation = input('Pick an operation: ')
        num2 = float(get_number('second'))

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        operation = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if operation == 'y':
            num1 = result
        if operation == 'n':
            keep_operating = False
            calculate()


calculate()
