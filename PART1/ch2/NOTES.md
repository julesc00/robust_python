# Notes from book Robust Python by Patrick Viafore 

# Introduction to Python Types

**Types**
Definition:
- A communication method
- They convey information
- They provide a representation that users and computers can reason about
  - *****Mechanical Representation*****: Types communicate behavior and constrains to the Python language itself.
  - *****Semantic Representation*****: Types communicate behavior and constrains to other developers.

**Behaviors of an ***int*****
- Constructible from integers, floats, or strings
- Mathematical operations such as addition, subtraction, division, multiplication, exponentiation, and negation
- Relational comparison such as `<, >, ==, !=`.
- Bitwise operations (manipulating individual bits of a number) such as `&, |, ^, ~,` and shifting.
- Converting to a string using `str` or `repr` functions.
- Able to be rounded through `ceil, floor` and `round` methods (even though they return 
    the integer itself, these are supported methods).

**Behaviors of ***datetime*****
- Constructible from a ***string, or a set of integers representing day/month/year/etc.***
- Mathematical operations such as addition and subtraction of ***time deltas.***
- Relational comparison.
- ***No bitwise*** operations available.
- Convertible to a string using `str` or `repr` functions.
- ***Is not*** able to be rounded through `ceil, floor` or `round` methods.

> ***Semantics*** refers to the meaning of an operation. 

*****Datetimes*** also support their own behaviors.**
- Changing values based on time zones.
- Being able to control the format of strings.
- Finding what weekday it is.