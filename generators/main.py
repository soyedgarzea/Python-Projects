from typing import Any, Generator, Literal


def make_list(num: int) -> list[int]:
    result: list[int] = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(10)


def generator_fn():
    for i in range(10):
        yield i


def fib(number: int) -> Generator[Literal[0, 1], Any, None]:
    a = 0
    b = 1

    for _ in range(number):
        yield a  # type: ignore
        temp = a # 0 1 1 2 3
        a = b # 1 1 2 3 5
        b = temp + b # 1 2 3 5 8


for x in fib(20):
    print(x)
