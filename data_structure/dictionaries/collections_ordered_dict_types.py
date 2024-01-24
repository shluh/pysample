'''
collections.OrderedDict: Remember the Insertion Order of Keys

Python includes a specialized dict subclass that remembers the insertion order of keys added to it: collections.OrderedDict.
Note: OrderedDict is not a built-in part of the core language and must be imported from the collections module in the standard library.
While standard dict instances preserve the insertion order of keys in CPython 3.6 and above, this was simply a side effect of the CPython implementation and was not defined in the language spec until Python 3.7. So, if key order is important for your algorithm to work, then it’s best to communicate this clearly by explicitly using the OrderedDict class:
'''

import collections
d = collections.OrderedDict(one=1, two=2, three=3)

d
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])

d["four"] = 4
d
# OrderedDict([('one', 1), ('two', 2),
            #  ('three', 3), ('four', 4)])

d.keys()
# odict_keys(['one', 'two', 'three', 'four'])