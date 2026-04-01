# ======================================== 5.1 List
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4

print(fruits.reverse())
print(fruits)

print(fruits.append('grape'))
print(fruits)

print(fruits.sort())
print(fruits)

print(fruits.pop())

fruits_copy = fruits.copy()
fruits_copy.remove('banana')
print(fruits_copy)

fruits_copy.clear()
print(fruits_copy)

fruits_copy.extend(range(3))
print(fruits_copy)

# You might have noticed that methods like insert,
# remove or sort that only modify the list have no
# return value printed – they return the default None.
# [1] This is a design principle for all mutable data structures in Python.

# use as stack
stack2 = [3, 4, 5]
stack2.append(6)
stack2.append(7)
stack2.pop()
stack2.pop()

# use queue
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
queue.popleft()  # The first to arrive now leaves
queue.popleft()  # The second to arrive now leaves

# 5.1.3 List Comprehensions

# squares = []
# for x in range(10):
#     squares.append(x**2)
# Note that this creates (or overwrites) a variable named x that
# still exists after the loop completes. We can calculate the list
# of squares without any side effects using:

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

bi = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(bi)

# It's equivalent to
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

# ======================================== 5.2 del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a

# ======================================== 5.3 Tuples and Sequences
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
# t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
print(v[0][1])

# initiate
empty = ()
singleton = 'hello',  # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!' are packed together in a tuple.
# The reverse operation is also possible:
x, y, z = t
print(x)

# This is called, appropriately enough,
# sequence unpacking and works for any sequence on the right-hand side.
# Sequence unpacking requires that there are as many variables on the
# left side of the equals sign as there are elements in the sequence.
# Note that multiple assignment is really just a combination of tuple
# packing and sequence unpacking.

# ======================================== 5.4 set

# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};
# the latter creates an empty dictionary,
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
print('orange' in basket)
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)  # unique letters in a
print(a - b)  # letters in A, but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

c = {'hello'}
print(c)

# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# ======================================== 5.5 Dictionaries

# Extracting a value for a non-existent key by subscripting (d[key]) raises a KeyError.
# To avoid getting this error when trying to access a possibly non-existent key,
# use the get() method instead, which returns None (or a specified default value)
# if the key is not in the dictionary.

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

# If there is no corresponding pair,KeyError is raised. Use "get" instead
# print(tel['irv'])
print(tel.get('irv'))

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))
print(sorted(tel))

print('guido' in tel)
print('jack' not in tel)

# empty dict
print({})

# use dict + sequence
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# dict comprehensions
print({x: x ** 2 for x in range(5)})

# keyword arguments
print(dict(sape=4139, guido=4127, jack=4098))

# ======================================== 5.6 Looping Techniques

# items
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# enumerate return the item and index
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# be paired with zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# reverse a sequence
for i in reversed(range(1, 10, 2)):
    print(i)

# eliminate duplicate elements and sort
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead.
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


# ======================================== 5.7 More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)


# ======================================== 5.8 Comparing Sequence and Other Types
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)