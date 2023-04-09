# Notes from book Robust Python by Patrick Viafore


# Chapter 1: ***Introduction to Robust Python***

## Collection choosing

**List**
- This is a collection to be iterated over. Very rarely do you expect to be retrieving specific elements
    from the middle of the list (using static list index).

**String**
- An immutable collection of characters.

**Generator**
- A collection to be iterated over, and never indexed into. They are great for computational expensive or
    infinite collections. An online database of recipes might be returned as a generator for example.

**Tuple**
- An immutable collection. You do not expect it to change, so it is more likely to extract specific
    elements from the middle of the tuple (either through indices or unpacking). It is very rarely
    iterated over. The information about a specific cookbook might be represented as a tuple such as
    (cookbook_name, author, page, count).

**Set**
- An iterable collection that contains no duplicates. You cannot rely on ordering of elements. The
  ingredients in a cookbook might be stored in a set.

**Dictionary**
- A mapping from keys to values. Keys are unique across the dictionary. Dictionaries are typically
    iterated over, or indexed into using dynamic keys. A cookbook's index is a great example of a
    key to value mapping (ei. from topic to page number).

### Special collection types that are expressive in communicating to the future:
**frozenset**
- A set that is immutable

**OrderedDict**
- A dictionary that preserves order of elements based on insertion time. As of CPython 3.6 and Python 3.7,
    built-in dictionaries will also preserve order of elements based on insertion time.

**defaultdict**
- A dictionary that provides a default value if the key is missing. for example:
```from collections import defaultdict
 def create_author_count_mapping(cookbooks: List([Cookbook])):
     counter = defaultdict(lambda: 0)
     for cookbook in cookbooks:
         counter[cookbook.author] += 1
     return counter
   ```

## Iteration
**for ***loops*****
- for loops are used for iterating over each element in a collection or range and performing an action/side effect.
```
for cookbook in cookbooks:
    print(cookbook)
```
** while ***loops*****
- while loops are used for iteratin as long as a certain condition is true.
```
while is_cookbook_open(cookbook):
    narrate(cookbook)
```
**Comprehensions**
- Comprehensions are used for transforming one collection into another (normally, this does not have
    side effects, specially if the comprehension is lazy).
`authors = [cookbook.author for cookbook in cookbooks]`

**Recursion**
- Recursion is used when the substructure of a collection is identical to the structure of a collection
  (ei. each child of a tree is also a tree):
```
def list_ingredientes(item):
    if isinstance(item, PreparedIngredient):
        list_ingredients(item)
    else:
        print(ingredient)
```
