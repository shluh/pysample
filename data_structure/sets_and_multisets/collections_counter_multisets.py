'''
collections.Counter: Multisets

The collections.Counter class in the Python standard library implements a multiset, or bag, type that allows elements in the set to have more than one occurrence.

This is useful if you need to KEEP TRACK of not only if an element is part of a set, but also how many times it’s included in the set:
'''


from collections import Counter
inventory = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
inventory
# Counter({'bread': 3, 'sword': 1})

more_loot = {"sword": 1, "apple": 1}
inventory.update(more_loot)
inventory
# Counter({'bread': 3, 'sword': 2, 'apple': 1})

