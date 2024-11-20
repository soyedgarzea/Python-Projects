'''
     _summary_

    _extended_summary_
'''
print('Welcome to Python Pizza Deliveries!')

bill = 0
size = input('What size pizza do you want? S, M or L: ').lower()
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ').lower()
extra_cheese = input('Do you want extra cheese? Y or N: ').lower()

if size == 's':
    bill += 15
    print('You ordered a small pizza')
elif size == 'm':
    bill += 20
    print('You ordered a medium pizza')
elif size == 'l':
    bill += 25
    print('You ordered a large pizza')

if pepperoni == 'y':
    if size == 's':
        bill += 2
    elif size in ('m', 'l'):
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f'Your final bill is {bill}')
