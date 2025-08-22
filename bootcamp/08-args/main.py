'''
    _summary_

_extended_summary_
'''


def greet():
    '''
    greet _summary_

    _extended_summary_
    '''
    print('Leila McKinney')
    print('Lulu Collier')
    print('Theodore Warren')


greet()


def greet_with_name(name):
    '''
    greet_with_name _summary_

    _extended_summary_

    Args:
        name (_type_): _description_
    '''
    print(f"Hello {name}")


greet_with_name('Edgar')


def greet_with(name, location):
    '''
    greet_with _summary_

    _extended_summary_

    Args:
        name (_type_): _description_
        location (_type_): _description_
    '''
    print(f"Hi, {name}")
    print(f"What is it like in {location}?")


# Positions arguments
greet_with('Edgar', 'México')

# Keyword arguments
greet_with(name='Edgar', location='México')
