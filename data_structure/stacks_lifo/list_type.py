'''
Python's built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time.

Python's lists are implemented as dynamic arrays internally, which means they occasionally need to resize the storage space for elements stored in them when elements are added or removed. The list over-allocates its backing storage so that not every push or pop requires resizing. As a result, you get an amortized O(1) time complexity for these operations.

The downside is that this makes their performance less consistent than the stable O(1) inserts and deletes provided by a linked list–based implementation (as you'll see below with collections.deque). On the other hand, lists do provide fast O(1) time random access to elements on the stack, and this can be an added benefit.

There's an important performance caveat that you should be aware of when using lists as stacks: To get the amortized O(1) performance for inserts and deletes, new items must be added to the end of the list with the append() method and removed again from the end using pop(). For optimum performance, stacks based on Python lists should grow towards higher indexes and shrink towards lower ones.

Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around to make room for the new element. This is a performance antipattern that you should avoid as much as possible:
'''


s = []
s.append("eat")
s.append("sleep")
s.append("code")

# print >>> ['eat', 'sleep', 'code']

s.pop()
# print >>> 'code'

s.pop()
# print >>> 'sleep'

s.pop()
# print >>> 'eat'

s.pop()
# print >>> IndexError: pop from empty list
