# name = input('What is your name?')

# print('Hello ' + name)

# Convert to binary
print(bin(5))

# Formatted strings
name = 'Edgar'
age = 30

print(f'Hi, {name}. You are {age} years old')
print('Hi, {1}. You are {0} years old'.format(name, age))
print('Hi, {name}. You are {age} years old'.format(name = 'Arturo', age = 29))

string = '0123456789'
print(string[0]) # -> start
print(string[0:2]) # -> end
print(string[0:8:2]) # -> jumps
print(string[::-1]) # -> reverse

# string[0] = '5' # -> Error

quote = 'something me'

quote.upper()
quote.capitalize()
quote.find('me')
quote.replace('me', 'you')

print(quote)

birthday = input('What year were you born? ');
age = 2024 - int(birthday)

print(f'You\'re {age} years old')

username = input('What is your username? ')
password = input('What is your password? ')
secret_password = '*' * len(password)

print(f'{username}, your password {secret_password} is {len(password)} letters long')
