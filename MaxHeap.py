MAX_SIZE = 1000

'''
An abstract implementation of a maximum heap.
In order to use this class you will need to:
    1. Implement the missing methods in MaxHeap.cpp. These are: remove, 
    increaseKey and remove_max methods.
    2. Inherit from MaxHeap, the inheritance should contain implementations 
    at least of the virtual function "compareProcesses".
'''

class MaxHeap:
    def __init__(self):
        '''Constructor'''
        self._elements = 0
        self._array = []

    def destroy(self):
        del self._array

    def left(self, root):
        #returns left son
        if root < 1 or root > self._elements:
            print 'left: invalid index %d \n' % root
            return -1
        if self._elements >= 2 * root:
            return root * 2
        else:
            return -1

    def right(self):
        #returns right son
        if root < 1 or root > self._elements:
            print 'right: invalid index %d \n' % root
            return -1
        if self._elements >= 2 * root + 1:
            return root * 2 + 1
        else:
            return -1


    def parent(self):
        if root < 1 or root > self._elements:
            print 'parent" invalid index %d \n' % root
            return -1
        return root / 2

    def insert(self, item):
        #inserts a new process into the heap and returns its index
        if self.IsFull():
            print 'insert: cannot insert, heap has reaches its limit \n'
            return -1
        self._elements += 1
        #elements represents the array position after the last 
        self._array[self._elements] = item
        new_pos = self._elements;

        while new_pos != 1 and self.compareProcesses(self._array[new_pos], self._array[self.parent(new_pos)]) > 0:
            self.swap_(new_pos, self.parent(new_pos));
            new_pos = parent(new_pos);
        return new_pos


    def increaseKey(self, index):
        '''
        The increaseKey function updates the heap with a process with 
        a larger priority in index.
        The method assumes that the new process's key is larger than 
        the key of the current process at array[index].
        '''
        pass
    def remove_max(self):
        pass
    def remove(self, member):
        pass
    def IsEmpty(self):
        return self._elements == 0

    def IsFull(self):
        return self._elements >= MAX_SIZE

    def count(self):
        return self._elements

    def printHeap(self):
        pass
    def compareProcesses(self, process1, process2):
        '''
        A comparison method you must implement in order to use the heap.
        The method receives two process references and returns:
        - a positive number if p1's key is larger than p2's key
        - 0 if p1's key is equal to p2's key
        - a negative number if p1's key is smaller than p2's key
        You must decide on the criteria for comparing the processes.
        '''
        pass

    def heapify(self, root):
        if root < 1:
            print 'heapify: invalid index %d \n' % root
            return
        if root > (self._elements/2):
            return # a leaf - no point in performing heapify

        largest = root
        if self.left(root) > 0 and self.compareProcesses(self._array[self.left(root)], self._array[largest]) > 0:
            largest = self.left(root)
        if self.right(root) > 0 and self.compareProcesses(self._array[self.right(root)], self._array[largest]) > 0:
            largest = self.right(root)
        if largest != root:
            self.swap_(root, largest)
            self.heapify(largest)
        return


    def getPos_(self, i):
        if i < 1 or i > self._elements:
            print 'getPos: invalid index %d \n' % i
            return None
        return self._array[i]

    def swap_(self, index1, index2):
        if index1 < 1 or index1 > self._elements or index2 < 1 or index2 > self._elements:
            print 'swap: invalid indexes %d %d \n' % index1 % index2
            return
        temp = self._array[index1]
        self._array[index1] = self._array[index2]
        self._array[index2] = temp

def main():
    heap = MaxHeap()

if __name__ == '__main__':
    main()