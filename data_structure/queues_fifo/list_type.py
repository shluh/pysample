# list: Terribly Sloooow Queues
'''
It's possible to use a regular list as a queue, but this is not ideal from a performance perspective. 
Lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all the other elements by one, requiring O(n) time.

Therefore, I would not recommend using a list as a makeshift queue in Python unless you’re dealing with only a small number of elements:
'''

q = []
q.append('eat')
q.append('sleep')
q.append('code')

print(q)

# Careful: This (q.pop) is slow!
print(q.pop(0))
