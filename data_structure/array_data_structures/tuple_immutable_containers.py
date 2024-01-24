'''
tuple: Immutable Containers

Just like lists, tuples are part of the Python core language. Unlike lists, however, Python’s tuple objects are immutable. This means elements can’t be added or removed dynamically—all elements in a tuple must be defined at creation time.
Tuples are another data structure that can hold elements of arbitrary data types. Having this flexibility is powerful, but again, it also means that data is less tightly packed than it would be in a typed array:
'''

arr = ("one", "two", "three")
arr[0]
# 'one'

# Tuples have a nice repr:
arr
# ('one', 'two', 'three')

# Tuples are immutable:
arr[1] = "hello"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

del arr[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object doesn't support item deletion

# Tuples can hold arbitrary data types:
# (Adding elements creates a copy of the tuple)
arr + (23,)
# ('one', 'two', 'three', 23)