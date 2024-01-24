''''
A set is an UNordered collection of objects that doesn't allow duplicate elements. 
Typically, sets are used to quickly test a value for membership in the set, to insert or delete new values from a set, and to compute the union or intersection of two sets.

In a proper set implementation, membership tests are expected to run in fast O(1) time. 
Union, intersection, difference, and subset operations should take O(n) time on average. 
The set implementations included in Python's standard library follow these performance characteristics.


set: Your Go-to Set
The set type is the built-in set implementation in Python. It's mutable and allows for the dynamic insertion and deletion of elements.
Python's sets are backed by the dict data type and share the same performance characteristics. Any hashable object can be stored in a set:


'''

vowels = {"a", "e", "i", "o", "u"}
"e" in vowels
# True

letters = set("alice")
letters.intersection(vowels)
# {'a', 'e', 'i'}

vowels.add("x")
vowels
# {'i', 'a', 'u', 'o', 'x', 'e'}

len(vowels)
# 6