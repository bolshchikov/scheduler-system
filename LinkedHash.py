'''
An abstract chain hash implementation for process objects.
In order to use it you will need to:
    1. Implement the missing function "remove" in LinkedHash.cpp
    2. You must inherit from this class and implement the hashFunction.
See further documentation below.
'''

class LinkedHashEntry:
    '''Constructor'''
    def __init__(self, key, value):
        # this identifies the element, is is NOT the hash key/value
        self._key = key 
        self._value = value
        self._next = None

    def getKey (self):
        return self._key

    def getValue (self):
        return self._value

    def setValue (self, p):
        self._value = p

    def getNext (self):
        return self._next

    def setNext (self, next):
        self._next = next


class LinkedHash:
    def __init__ (self, maxSize):
        '''Constructor'''
        self._max_size = maxSize
        #python's vars are dynamic, so no need to go over 
        #the whole table and fill it with NULLs
        self._table = [] 
    
    def destroy (self):
        '''Removes all members of hashtable'''
        pass
    
    def hashFunction (self, key):
        '''You must implement this function in the derived class 
        in order to use the hash.
        What are the assumptions you are making ?
        What will be your key ?''' 
        pass

    def get (self, key):
        '''Returns the process corresponding to key.
        You need to decide on the key to provide to this function.'''
        pass

    def insert (self, key, value):
        '''Inserts a new process to the hashtable.
        You need to decide on the key to provide to this function.'''
        #while adding, due to dynamoc nature of an array, 
        #have to check all the time whether max_size is not exceeded
        pass

    def remove (self, key):
        '''Removes an existing process from the hashtable.
        You need to implement it in LinkedHash.cpp.'''
        pass

    def getMaxSize (self):
        return self._max_size