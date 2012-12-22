class Process:
    '''Needs to be implemented by students'''
    def __init__(self, id, priority, creationNum):
        self._id = id
        self._priority = priority
        self._creationNum = creationNum
        self._creationPosition = 0
        self._priorityPosition = 0

    def changePriority (self, newPriority):
        self._priority = newPriority if newPriority > 0 else self._priority
    
    def getID (self):
        return self._id
    
    def getPriority (self):
        return self._priority

    def getCreationNum (self):
        return self._creationNum

    def getCreationPosition (self):
        return self._creationPosition

    def getPriorityPosition (self):
        return self._priorityPosition

    def setCreationPosition (self, index):
        self._creationPosition = index

    def setPriorityPosition (self, index):
        self._priorityPosition = index