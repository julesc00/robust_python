from typing import Iterable


# Example One of Duck typing
def print_items(items: Iterable):
    for item in items:
        print(item)


print_items([1, 2, 3])
print_items({4, 5, 6})
print_items({
    "A": 1,
    "B": 2,
    "C": 3
})
print_items("Hello")


# Example 2 of Duck typing
def double_value(value):
    return value + value


print(double_value(5))
print(double_value("Hello"))
print(double_value([1, 2, 3]))
