# Comprehension

my_list = [char for char in 'hello']

print(my_list)  # -> ['h','e','l','l','o']


my_list_2 = [num**2 for num in range(0, 100)]
print(my_list_2)

my_list_3 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list_3)


my_set = {num**3 for num in range(0, 20) if num % 3 == 0}


my_dict = {
    'a': 1,
    '2': 2,
}

new_dict = {key: value**2 for key, value in my_dict.items()}


cool_dict = {num: num*2 for num in [1, 2, 3]}


chars = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([char for char in chars if chars.count(char) > 1]))

print(duplicates)
