MAX_SIZE = 1000

'''
An abstract implementation of a maximum heap.
In order to use this class you will need to:
    1. Implement the missing methods in MaxHeap.cpp. These are: remove, increaseKey and remove_max methods.
    2. Inherit from MaxHeap, the inheritance should contain implementations at least of the virtual function
        "compareProcesses".
'''

class MaxHeap:
	def __init__(self):
		self.elements = 0
	def destroy(self):
		pass
	def left(self):
		#returns left son
		pass
	def right(self):
		#returns right son
		pass
	def parent(self):
		pass
	def insert(self, process):
		#inserts a new process into the heap and returns its index
		pass
	def increaseKey(self, index):
		'''The increaseKey function updates the heap with a process with a larger priority in index.
   		The method assumes that the new process's key is larger than the key of the current
   		process at array[index].'''
		pass
	def remove_max(self):
		pass
	def remove(self, member):
		pass
	def IsEmpty(self):
		pass
	def IsFull(self):
		pass
	def count(self):
		pass
	def printHeap(self):
		pass
	def compareProcesses(self, process1, process2):
		'''A comparison method you must implement in order to use the heap.
    	The method receives two process references and returns:
	    - a positive number if p1's key is larger than p2's key
	    - 0 if p1's key is equal to p2's key
	    - a negative number if p1's key is smaller than p2's key
		You must decide on the criteria for comparing the processes.'''
		pass
	def heapify(self, root):
		pass
	def getPos_(self, index):
		pass
	def swap_(self, index1, index2):
		pass