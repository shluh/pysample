'''
collections.deque: Fast and Robust Queues
linked list-based implementation

The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). 
Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python's deque objects are implemented as DOUBLY-LINKED LISTS. This gives them excellent and consistent performance for inserting and deleting elements, 
but poor O(n) performance for randomly accessing elements in the middle of the stack.
As a result, collections.deque is a great default choice if you’re looking for a queue data structure in Python’s standard library:
'''

from collections import deque

q = deque()
q.append("eat")
q.append("sleep")
q.append("code")

print(q[0])

print(q.popleft()) #"eat"
print(q[0])

# print(q.popleft()) #"sleep"
# print(q.popleft()) #"code"
# print(q.popleft()) #IndexError: pop from an empty deque
