print('Welcome to the tip calculator!')
bill = int(input('What is the total bill? $'))
tip = int(input('How much tip would you like to give? 5, 10, 15, 20? '))
people = int(input('How many people to split the bill? '))

convert_tip = 1.00 + tip / 100
total = bill * convert_tip
bill_per_person = total / people

print(f'Each person should pay: ${round(bill_per_person, 2)}')
