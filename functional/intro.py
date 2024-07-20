from functools import reduce

# Pure Functions
# This FN doesn't interact with outside context


def multiply_by2(li: list[int]):
    '''
    multiply_by2 _summary_

    _extended_summary_

    Args:
        li (list[int]): _description_

    Returns:
        _type_: _description_
    '''
    new_list: list[int] = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))


# MAP
def multiply_by3(item: int) -> int:
    return item * 3


print(list(map(multiply_by3, [1, 2, 3])))  # -> Map creates a new list [3,6,9]


# FILTER


def find_even(item: int) -> int:
    return item % 2 == 0


print(list(filter(find_even, [1, 2, 3, 4, 5])))


# ZIP
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
print(list(zip(list_1, list_2, list_3)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)] -> zip creates a tuple of the same length as

# REDUCE


def accumulate(acc: int, item: int) -> int:
    return acc + item


print(reduce(accumulate, list_1, 0))
