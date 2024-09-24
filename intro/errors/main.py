# Error Handling

# TypeError
# SyntaxError
# NameError
# IndexError
# KeyError
# ZeroDivisionError

try:
    age = int(input('What is your age?'))
    print(age)
    # raise ValueError('custom error)
except:  # pylint: disable=bare-except
    print('Please enter a number')
else:
    print('Thank you')
finally:
    print('This will always run')
