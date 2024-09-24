file1 = open('test.txt', encoding='UTF-8')
print(file1)

print(file1.read())
file1.seek(0) # -> return to init
print(file1.read())

file1.close()

file2 = open(file='test2.txt', encoding='UTF-8')
print(file2)

print(file2.readline())
print(file2.readline())
print(file2.readlines())
file2.close()

with open('./working_with_files/test3.txt', encoding='UTF-8', mode='a+') as file3: # 'r' -> default
    file3.write('\nHello, world!')

file3_read = open('test3.txt', encoding='UTF-8')
print(file3_read.readlines())
