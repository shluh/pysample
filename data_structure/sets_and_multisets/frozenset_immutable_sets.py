''''
frozenset: Immutable Sets
The frozenset class implements an immutable version of set that can’t be changed after it’s been constructed.

frozenset objects are static and allow only query operations on their elements, not inserts or deletions. Because frozenset objects are static and hashable, they can be used as dictionary keys or as elements of another set, something that isn’t possible with regular (mutable) set objects:

'''

vowels = frozenset({"a", "e", "i", "o", "u"})
vowels.add("p")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'

# Frozensets ARE HASHABLE and can
# be used as dictionary keys:
d = { frozenset({1, 2, 3}): "hello" }
d[frozenset({1, 2, 3})]
# 'hello'

