'''
dict: Your Go-to Dictionary

Because dictionaries are so important, Python features a robust dictionary implementation that's built directly into the core language: the dict data type.
Python also provides some useful syntactic sugar for working with dictionaries in your programs. For example, the curly-brace ({ }) dictionary expression syntax and dictionary comprehensions allow you to conveniently define new dictionary objects:

Python dictionaries are based on a well-tested and finely tuned hash table implementation 
    that provides the performance characteristics you'd expect: O(1) time complexity for 
        lookup, insert, update, and delete operations in the AVERAGE case.

'''

phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}
phonebook["alice"]
# 3719

squares
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}