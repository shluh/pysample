'''
collections.deque: Fast and Robust Stacks
The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). 
Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python's deque objects are implemented as doubly-linked lists, which gives them excellent and consistent performance for
 inserting and deleting elements but poor O(n) performance for randomly accessing elements in the middle of a stack.

Overall, collections.deque is a great choice if you're looking for a stack data structure in Python's standard library that has 
the performance characteristics of a linked-list implementation:
'''

from collections import deque
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")

print(s)
# deque(['eat', 'sleep', 'code'])

print(s.pop())
# 'code'
print(s.pop())
# 'sleep'
print(s.pop())
# 'eat'

print(s.pop())
#IndexError: pop from an empty deque
