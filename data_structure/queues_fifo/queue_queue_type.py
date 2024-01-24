'''
queue.Queue: Locking Semantics for Parallel Computing
The queue.Queue implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.

The queue module contains several other classes implementing multi-producer, multi-consumer queues that are useful for parallel computing.

Depending on your use case, the locking semantics might be helpful or just incur unneeded overhead. 
In this case, you’d be better off using collections.deque as a general-purpose queue:
'''

from queue import Queue

q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")

print(q)
print(q.get())
print(q.get())
print(q.get())

'''
https://docs.python.org/3/library/queue.html#queue.Queue.get_nowait
Equivalent to get(False).

Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.
'''
print(q.get_nowait())
# >>> queue.Empty

print(q.get())


