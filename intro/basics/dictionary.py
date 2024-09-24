dictionary = {
  'a': 1,
  'b': 2,
  'x': 3
}

print(dictionary)

print(dictionary.get('age', 55)) # -> get(key, default value)

user = dict(name='Edgar')

print(user)
print('size' in user)
print('name' in user.keys())
print(user.items())

person = {
  'name': 'Edgar',
  'age': 25,
}
person_copy = person.copy()
person.clear()

print(person, person_copy)
person_copy.update({'age': 30})
person_copy.update({'car': 'Ibiza'})
print(person_copy)
# person_copy.pop('dog') -> Throws error
# print(person_copy)
person_copy.popitem()
print(person_copy)
