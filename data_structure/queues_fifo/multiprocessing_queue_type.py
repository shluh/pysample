'''
multiprocessing.Queue: Shared Job Queues

multiprocessing.Queue is a shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers.
Process-based parallelization is popular in CPython due to the global interpreter lock (GIL) that prevents some forms of parallel execution on a single interpreter process.

As a specialized queue implementation meant for sharing data between processes, multiprocessing.Queue makes it easy to distribute work across multiple processes in order to work around the GIL limitations. This type of queue can store and transfer any pickleable object across process boundaries:

'''

from multiprocessing import Queue

q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")

print(q)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
