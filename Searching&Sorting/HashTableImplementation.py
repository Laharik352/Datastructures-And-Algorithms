'''Implementation of Hash Tables
The idea of a dictionary used as a hash table to get and retrieve items using keys is often
referred to as a mapping. In our implementation we will have the following methods:

HashTable() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored
in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.'''

# class HashTable(object):
#
#     def __init__(self, size):       #initializing our hash table
#         self.size = size
#         self.slots = [None] * self.size #[None, None.....]
#         self.data = [None] * self.size
#
#     def put(self, key, data): # To put in a piece of data to the correct key
#
#         hashvalue = self.hashfunction(key, len(self.slots))
#
#         if self.slots[hashvalue] == None:       #If the slot is empty, we fill in the key and the data in the corresponding slot
#             # print(key, data)
#             self.slots[hashvalue] = key
#             self.data[hashvalue] = data
#
#         else:       #If the key already exists, we go ahead and replace the old value
#
#             if self.slots[hashvalue] == key:
#                 self.slots[hashvalue] = data
#
#             else:       # If the key does not exist, we go ahead and find the next available slot
#
#                 nextslot = self.rehash(hashvalue, len(self.slots)) #When a collission occurs, we get into the next slot
#
#                 while self.slots[nextslot] != None and self.slots[nextslot] != key: #To find the next empty slot
#                     nextslot = self.rehash(nextslot, len(self.slots))
#
#                 if self.slots == None:
#                     self.slots[nextslot] = key
#                     self.data[nextslot] = data
#                 else:
#                     self.data[nextslot] = data
#
#
#     def hashfunction(self, key, size):  # Remainder method
#         return key%size
#
#     def rehash(self, oldhash, size):
#         return (oldhash+1)%size
#
#     def get(self, key):     # To find the data given the key
#         startslot = self.hashfunction(key, len(self.slots))     # To tell what start do we start off in our search
#         data = None
#         stop = None
#         found = None
#         position = startslot
#
#         while self.slots[position] != None and not found and not stop:  #Continue as long as it is not empty
#
#             if self.slots[position] == key:
#                 found = True
#                 data = self.data[position]
#
#             else:
#                 position = self.rehash(position, len(self.slots))   #Continue to the next slot
#                 if position == startslot:
#                     stop = True
#         return data
#
#     def __getitem__(self, key):
#         return self.get(key)
#
#     def __setitem__(self, key, data):
#         self.put(key,data)
#
# h = HashTable(5)
# h[1] = 'One'
# h[2] = 'Two'
# h[3] = 'Three'
# print(h[1])
# print(h[2])
# print(h[3])

'''More easier way to implement a hashmap in python'''
# https://www.youtube.com/watch?v=9HFbhPscPU0
# Hash Map

class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
print(h.keys())

