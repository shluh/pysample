'''
01 - Design a data structure that supports the following operations add/search/delete where all operations complete in O(1) time.  
02 - It should only contain one distinct instance of a value at a time.
03 - It should have the behavior of a FIFO buffer, and if an item is removed and replaced it is added to the end of the buffer.

So if a the structure has this state
1 2 3 4 5

And 3 is added the state becomes
1 2 4 5 3
'''

'''
>>> Requirements <<<

01 - the following operations add/search/delete where all operations complete in O(1) time.
Python dictionaries are based on a well-tested and finely tuned hash table implementation that 
    provides the performance characteristics you'd expect: O(1) time complexity 
        for lookup, insert, update, and delete operations in the average case.
ref: https://realpython.com/python-data-structures/#dictionaries-maps-and-hash-tables
        
02 - It should only contain one distinct instance of a value at a time.
Dictionaries cannot have two items with the same key
ref: https://www.w3schools.com/python/python_dictionaries.asp

03 - It should have the behavior of a FIFO buffer (^ Python3.8)
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
ref: https://www.w3schools.com/python/python_dictionaries.asp

'''

class DataStructure:
    def __init__(self):      
        self.my_dicty = {}

    def add(self, x):
        self.my_arr.append(x)
        self.my_dicty[x] = self.my_arr.index(x)

    def search(self, x):
        return self.my_dicty.get(x, None)
    
    def delete_by_key(self, x):  
        self.my_dicty.pop(x)

    def delete(self):   
        self.my_dicty.popitem(last=False)
        

