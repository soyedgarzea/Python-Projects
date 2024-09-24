import re

pattern = re.compile('this')
string = 'search this inside of this text'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.match(string)

print(a) # type: ignore
print(a.group()) # type: ignore
print(b) # type: ignore
print(c) # type: ignore
