import math
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
        # this key identifies the element, is is NOT the hash key/value
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
        self._table = [None]*self._max_size 
    
    def destroy (self):
        '''Removes all members of hashtable'''
        if self._table == None:
            return
        for record in self._table:
            if record != None:
                prev = None
                entry = record
                while entry != None:
                    prev = entry
                    entry = entry.getNext()
                    if (prev.getValue() != None):
                        val = prev.getValue()
                        val = None
                    prev = None
        self._table = None


    
    def hashFunction (self, key):
        '''You must implement this function in the derived class 
        in order to use the hash.
        What are the assumptions you are making ?
        What will be your key ?''' 
        # multiplication method implementation
        return int(math.floor(self._max_size*((key*0.293)%1)))


    def get (self, key):
        '''Returns the process corresponding to key.
        You need to decide on the key to provide to this function.'''
        hashKey = self.hashFunction(key)
        if hashKey >= self._max_size or hashKey < 0:
            print 'hashFunction result cannot be larger than %d or negative \n' % self._max_size
            return None
        if self._table[hashKey] == None:
            return None
        else:
            entry = self._table[hashKey]
            while entry != None and entry.getKey() != key:
                entry = entry.getNext()
            if entry == None:
                return None
            else:
                return entry.getValue()


    def insert (self, key, value):
        '''Inserts a new process to the hashtable.
        You need to decide on the key to provide to this function.'''
        #while adding, due to dynamoc nature of an array, 
        #have to check all the time whether max_size is not exceeded
        hashKey = self.hashFunction(key)
        if hashKey >= self._max_size or hashKey < 0:
            print 'hashFunction result cannot be larger than %d or negative \n' % self._max_size
            return 
        p = self.get(key)
        
        if p != None:
            print 'Process with id %d alreay exists in the hash' % key
            return

        lhe = LinkedHashEntry(key, value)
        if self._table[hashKey] != None:
            head = self._table[hashKey]
            lhe.setNext(head)
        self._table[hashKey] = lhe

    def remove (self, key):
        '''Removes an existing process from the hashtable.
        You need to implement it in LinkedHash.cpp.'''
        hashKey = self.hashFunction(key)
        if hashKey >= self._max_size or hashKey < 0:
            print 'hashFunction result cannot be larger than %d or negative \n' % self._max_size
            return None
        if self._table[hashKey] == None:
            return None
        else:
            prev = None
            entry = self._table[hashKey]
            while entry != None and entry.getKey() != key:
                prev = entry
                entry = entry.getNext()
            if entry == None:
                return None
            else:
                if prev != None:
                    prev.setNext(entry.getNext());
                else:
                    self._table[hashKey] = entry.getNext()                 
                entry = None


    def getMaxSize (self):
        return self._max_size

    def printTable (self):
        for record in self._table:
            if record != None:
                entry = record
                while entry != None:
                    print (entry.getKey(), entry.getValue())
                    entry = entry.getNext()
            else:
                print None

def main():
    hash = LinkedHash(10)
    hash.insert(1, 'test')
    hash.remove(1)
    hash.printTable()

if __name__=='__main__':
    main()