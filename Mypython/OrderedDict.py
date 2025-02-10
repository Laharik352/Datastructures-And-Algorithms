'''
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that

Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.
'''


from collections import OrderedDict
#Using normal python dictionary
print("Normal dict")
ordered = {}
ordered['a'] = 1
ordered['b'] = 2
ordered['c'] = 3
ordered['d'] = 4
print("Before change")
for k,v in ordered.items():     #{'a': 1, 'c': 3, 'b': 2, 'd': 4}
    print(k,v)
ordered['a'] = 5
print("After change")
for k,v in ordered.items():     #{'a': 5, 'c': 3, 'b': 2, 'd': 4}
    print(k,v)

# Using ordered dict
print("Ordered dict")
ordered1 = OrderedDict()
ordered1['a'] = 1
ordered1['b'] = 2
ordered1['c'] = 3
ordered1['d'] = 4
print("Before change")
for k,v in ordered1.items():    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(k,v)
ordered1['a'] = 5
print("After change")
for k,v in ordered1.items():    #{'a': 5, 'b': 2, 'c': 3, 'd': 4}
    print(k,v)
