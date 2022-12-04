from ctypes import string_at
from sys import getsizeof
from binascii import hexlify
import datetime


a = 0b01010000_01000001_01010100

print(a)

# Prints out the memory of the variable
print(hexlify(string_at(id(a), getsizeof(a))))

text = "PAT"
print(hexlify(string_at(id(text), getsizeof(text))))


date_today = datetime.datetime.now()
past_date = datetime.datetime(2021, 9, 8, 22, 19, 28, 838667)
print(date_today)
print(past_date)


"""
Page 27 (book)
We need to add functionality to be able to change closing time (say for extending
a kitchen's ours on holidays).

Semantic expression is not clear in the following code.
"""


def closing_time():
    return datetime.datetime(2022, 12, 4)


def close_kitchen():
    pass


def log_time_closed(time: datetime.datetime):
    pass


# Suboptimal approach without types on parameter declaration
def close_kitchen_if_past_cutoff_time(point_in_time):
    if point_in_time >= closing_time():
        close_kitchen()


# Better approach
def close_kitchen_if_past_cutoff_time_v2(point_in_time: datetime.datetime):
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)


a: int = 5
print(type(a))

"""
End of section
"""