new_set = {1, 2, 2, 3}
print(new_set)
new_set.add(2)
new_set.add(100)

print(3 in new_set)


cars = {'Ibiza', 'Leon', 'Audi', 'Mini'}
motorcycles = {'Yamaha', 'Leon', 'Audi', 'Suzuki'}
skates = {'Yamaha', 'Bauer', 'Eaton', 'Suzuki'}
print(cars.difference(motorcycles))

cars.discard('Audi')


numbers = {1, 2, 3, 4, 5}
new_numbers = {4, 5, 6, 7, 8, 9}

numbers.difference_update(new_numbers)
print(numbers)

numbers.intersection(new_numbers)  # -> numbers & new_numbers

print(new_set.isdisjoint(new_numbers))  # -> Doesn't have intersections

print(new_set.union(numbers, new_numbers))  # new_set | numbers | new_numbers
print(cars | motorcycles | skates)

new_set.discard(100)
print(new_set.issubset(numbers))
print(numbers.issuperset(new_set))
