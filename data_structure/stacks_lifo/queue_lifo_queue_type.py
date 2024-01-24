'''
queue.LifoQueue: Locking Semantics for Parallel Computing
The LifoQueue stack implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.

Besides LifoQueue, the queue module contains several other classes that implement multi-producer, multi-consumer queues that are useful for parallel computing.

Depending on your use case, the locking semantics might be helpful, or they might just incur unneeded overhead. In this case, you’d be better off using a list or a deque as a general-purpose stack:

'''


from queue import LifoQueue
s = LifoQueue()
s.put("eat")
s.put("sleep")
s.put("code")

print(s)
#<queue.LifoQueue object at 0x108298dd8>

print( s.get())
#'code'
print( s.get())
#'sleep'
print( s.get())
#'eat'

print( s.get_nowait())
#queue.Empty

print( s.get())  # Blocks/waits forever...