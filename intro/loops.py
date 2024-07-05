for item in 'Edgar Arturo Mora Zea':
  print(item, 'string')

for item in [1,2,3,4,5]:
  print(item, 'lists')

for item in (1,2,3,4,5):
  print(item, 'tuples')

for item in {'a': 1}:
  print(item, 'dicts')

for item in {'a': 1}.items():
  print(item, 'dicts items')

for key, value in {'a': 1}.items():
  print(key, value, 'dicts items separately')

for item in {'a': 1}.values():
  print(item, 'dicts values')

for item in {1,2,3,4,5}:
  print(item, 'sets')

for number in range(0, 10):
  print(number)

for _ in range(2):
  print(list(range(10)))

for i, char in enumerate('Edgar'):
  print(i, char)

# WHILE

i = 0
while i <= 10:
  print(i)
  i += 1
else:
  print('i is no longer less than 10')
