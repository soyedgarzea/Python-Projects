numbers = (1,2,3,4,5,6,7,8,9,10) # -> Immutable

print(numbers[0])
print(5 in numbers)

even = numbers[1::2]
odd = numbers[0::2]
print(even, odd)

one,two, *rest = numbers

print(one, two, rest)

print(numbers.count(10))
print(numbers.index(1))
print(len(numbers))
