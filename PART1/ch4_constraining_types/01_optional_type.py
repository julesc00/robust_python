from typing import Optional
import logging

"""
Optional types offer you two choices: either you have a value or you don’t. In other
words, it is optional to set the variable to a value.

Advantages of using Optional:
    1. You communicate your intent more clearly.
    2. You are able to further distinguish the absence of value from an empty value.
"""

maybe_a_string: Optional[str] = "abc"  # This has a value
maybe_a_string2: Optional[str] = None  # This is the absence of a value
if not maybe_a_string:
    print(maybe_a_string2)
else:
    print(maybe_a_string)


def create_hot_dog():
    bun = dispense_bun()
    if bun is None:
        logging.error("Bun couldn't be dispensed")
        return
    frank = dispense_frank()
    hot_dog = bun.add_frank()
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)
