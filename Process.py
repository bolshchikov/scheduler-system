class Process:
    '''Needs to be implemented by students'''
    def __init__(self, id, priority, creationNum):
        self._id = id
        self._priority = priority
        self._creationNum = creationNum
        self._name = None

    def changePriority (self, newPriority):
        self._priority = newPriority if newPriority > 0 else self._priority
    
    def getID (self):
        return self._id
    
    def getPriority (self):
        return self._priority

    def getCreationNum (self):
        return self._creationNum