from ctypes import string_at
from sys import getsizeof
from binascii import hexlify
import datetime
import random


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


"""
Type annotations
"""

OWNER = ""


# Ambiguous example without type annotations
def schedule_restaurant_open(open_time, workers_needed):
    pass


# With type annotations
def schedule_restaurant_open_v2(open_time: datetime.datetime, number_of_workers_needed: int):
    workers = find_workers_available_for_time(open_time)
    # Use random.sample to pick X available workers
    # where X is the number of workers needed.
    for worker in random.sample(workers, number_of_workers_needed):
        worker.schedule(open_time)


def find_workers_available_for_time(open_time: datetime.datetime):
    return int


# Confusing code
def find_workers_available_for_time_v3(open_time: datetime):
    workers = workers_database.get_all_workers()
    available_workers = [worker for worker in workers if is_available(worker)]

    if available_workers:
        return available_workers

    # fall back to workers who listed they are available
    # in an emergency
    emergency_workers = [worker for worker in get_emergency_workers() if is_available(worker)]

    if emergency_workers:
        return emergency_workers

    # Schedule the owner to open, they will find someone else
    return [OWNER]


# With return type to avoid confusion
def find_workers_available_for_time_v4(open_time: datetime) -> list[str]:
    pass


"""
In Python 3.8 and earlier built-in collection types such as list, dict and
set did not allow bracket syntax such as list[Cook] or dict[str, int]. Instead,
you needed to use type annotations from the typing module:
"""
from typing import Dict, List


class Cookbook:
    pass


AuthorToCountMapping = Dict[str, int]


def count_authors(
        cookbooks: List[Cookbook]
) -> AuthorToCountMapping:
    pass


def get_ratio(val1, val2):
    return float(val1 / val2)


# We can also annotate variables when needed:
workers: list[str] = find_workers_available_for_time_v4(open_time=datetime)
numbers: list[int] = []

ration: float = get_ratio(5, 3)
