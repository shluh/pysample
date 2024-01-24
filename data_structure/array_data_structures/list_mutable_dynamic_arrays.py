'''
list: Mutable Dynamic Arrays

Lists are a part of the core Python language. Despite their name, 
    Python’s lists are implemented as DYNAMIC ARRAYS behind the scenes.

This means a list allows elements to be added or removed, 
    and the list will automatically adjust the backing store that holds 
    these elements by allocating or releasing memory.

Python lists can hold arbitrary elements—everything is an object in Python, 
    including functions. Therefore, you can mix and match different kinds 
    of data types and store them all in a single list.

This can be a powerful feature, but the downside is that supporting multiple 
    data types at the same time means that data is generally less tightly packed. 
    As a result, the whole structure takes up more space:    
'''