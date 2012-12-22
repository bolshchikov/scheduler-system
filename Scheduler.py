import MaxHeap
import LinkedHash
import Process

MAX_PROCS = 1000

class Scheduler:
    def __init__ (self):
        self._numOfProcs = 0
        self._creationNum = 0
        self._hash = LinkedHash.LinkedHash(MAX_PROCS/10)
        self._heapByPriority = MaxHeap.MaxHeap()
        self._heapByCreation = MaxHeap.MaxHeap()

    def destroy (self):
        self._hash.destroy()
        self._hash = None
        self._heapByCreation.destroy()
        self._heapByCreation = None
        self._heapByPriority.destroy()
        self._heapByPriority = None

    def addProcess (self, id, priority):
    	self._numOfProcs += 1
        self._creationNum -= 1
        process = Process.Process(id, priority, self._creationNum);
        self._heapByCreation.insert({'key': self._creationNum, 'value': process})
        self._heapByPriority.insert({'key': priority, 'value': process})
        self._hash.insert(id, process)

    def scheduleByCreation (self):
        '''
        1. Remove maximum from _heapByCreation
        2. Get its position in _heapByPriority from _hash
        3. Remove from _heapByPriority
        4. Remove from _hash
        5. Reduce amount of processes in the system
        6. Return the value
        '''
        maximumItem = self._heapByCreation.remove_max()
        priorityIndex = maximumItem['value'].getPriorityPosition()
        self._heapByPriority.remove(priorityIndex)
        self._hash.remove(maximumItem['value'].getID()) 
        self._numOfProcs -= 1
        return maximumItem['value'].getID()

    def scheduleByPriority (self):
        maximumItem = self._heapByPriority.remove_max()
        creationIndex = maximumItem['value'].getCreationPosition()
        self._heapByCreation.remove(creationIndex)
        self._hash.remove(maximumItem['value'].getID())
        self._numOfProcs -= 1
        return maximumItem['value'].getID()

    def changePriority (self, id, newPriority):
        '''
        1. Retrieve process from a hash by id
        2. Call increaseKey method of heapByPriority
        3. Call changePriority method of process class
        '''
        process = self._hash.get(id)
        self._heapByPriority.increaseKey(process.getPriorityPosition(), newPriority);
        process.changePriority(newPriority)

    def killProcess (self, id):
        process = self._hash.get(id)
        if process:
            self._heapByPriority.remove(process.getPriorityPosition())
            self._heapByCreation.remove(process.getCreationPosition())
        else:
            print 'killProcess: process with id %d is not in the scheduler' % id

    def numOfProcesses (self):
        return self._numOfProcs