a = 'Hello'

if (n:=len(a) > 10):
  print(f'a is longer than 10 -> {n}')

while ((n := len(a)) > 0):
  print(a)
  a = a[:-1]
