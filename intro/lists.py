amazon_cart = ['books', 'magazines', 'clothes']
print(amazon_cart[0::2]);

amazon_cart[0] = 'laptops'
print(amazon_cart)

new_cart = amazon_cart[1:3] # Avoid passing by reference
print(new_cart)

# Adding
list_1 = [1]
list_1.append(2)
print(list_1)

# inserting

list_2 = [1]
list_2.insert(0, 2)
print(list_2)

# extending
list_3 = [1]
list_3.extend([2, 3])
print(list_3)

# removing - pop
list_4 = [1, 2, 3]
list_4.pop()
print(list_4)

# removing - remove
list_5 = [1, 2, 3]
list_5.remove(2)
print(list_5)

# clear
list_6 = [1, 2, 3]
list_6.clear()
print(list_6)

# index
list_7 = ['a', 'b', 'c', 'd', 'e']
print(list_7.index('c'))
print(list_7.index('c', 0))
print(list_7.index('c', 0, len(list_7)))
# print(list_7.index('c', 0, 1)) -> throws error

# in
list_8 = ['a', 'b', 'c', 'd', 'e']
print('f' in list_8)

# count
list_9 = ['a', 'b', 'c', 'd', 'e']
print(list_9.count('a'))

# sort
list_10 = [1, 20, 3, 4, 5]
list_10.sort() # Modifies list
print(list_10)

# sorted
list_11 = [1, 20, 3, 4, 5]
print(sorted(list_11)) # Returns a new list

# copy
list_12 = [1, 2, 3]
list_13 = list_12.copy()
print(list_13)

# reverse
list_14 = [1, 2, 3]
list_14.reverse()
print(list_14)

# reverse with slicing
list_15 = [1, 3, 2, 5, 10, 6]
list_15.sort()
print(list_15[::-1], list_15)

# range
print(list(range(10)))

# join
list_16 = ['a', 'b', 'c']
print(''.join(list_16))

sentence = ' '
new_sentence = sentence.join(['hi', 'Edgar'])
print(new_sentence)

# list unpacking
a,b,c, *d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a,b,c,d, e)
