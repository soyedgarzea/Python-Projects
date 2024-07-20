def greet():
    print('Hello')


greet()


def greet_2(name: str, emoji: str = '😀'):
    print(f'Hello {name} {emoji}')


greet_2('Edgar')


def custom_sum(num_1: int, num_2: int):
    return num_1 + num_2


print(custom_sum(5, 10))


def quadratic(num1: int, num2: int):
    sum = num1 + num2

    def elevate():
        return sum * 2
    return elevate


result = quadratic(1, 2)
print(result())


def user_greet():
    print('Hello')


user = {
    'greet': user_greet
}


def test(string: str):
    '''
    Information
    '''
    print(string)


test('!!!')
print(test('!!!'))
print(test.__doc__)

# params, *args, default params, **kwargs


def multiple_args(*args, **kwargs):  # type: ignore
    total = 0
    for item in kwargs.values(): # type: ignore
        total += item  # type: ignore
    return sum(args) + total  # type: ignore


print(multiple_args(1, 2, 3, 4, 5, num1=5, num2=10))  # type: ignore


def highest_even(numbers: list[int]):
    evens: list[int] = []
    highest = 0
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        if number % 2 == 0 and number > highest:
            highest = number
    return (highest, max(evens))


print(highest_even([10, 1, 2, 3, 5, 20]))


count = 0


def using_global():
    global count
    count += 1
    return count


print(using_global())


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print('outer:', x)


outer()
