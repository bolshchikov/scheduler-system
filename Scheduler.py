class Scheduler:
	def __init__ (self):
		self._numOfProcs = 0

	def destroy (self):
		pass

	def addProcess (self, id, priority):
		pass

	def scheduleByCreation (self):
		pass

	def scheduleByPriority (self):
		pass

	def changePriority (self, id, newPriority):
		pass

	def killProcess (self, id):
		pass

	def numOfProcesses (self):
		return self._numOfProcs