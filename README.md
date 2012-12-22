Process scheduling system
=============================

* * *
### Description
You have to write the system that implements the process scheduler. There might be several processes running at the same time
on the computer, however, at certain point of time only one of them is being processed. The scheduler must decide regarding the 
processes either based on its priority or creating order.

*For example*: Actions which are initiated by user (opening a browser) should receive a higher priority to compare with process
of anti-virus system scanning, which should receive lower priority since it's not urgent for a user to get the response. 

Each process, at the time of creation, receives the unique id number, which is created by the schedular system. Besides that
priority is defined at each process which reflects its urgency. 
Right adter the process is created, it is passed to the scheduler system, which recognize them according to id number.
You should create the system which performs the operations mentioned further.

### Assumptions
*	In all methods below, *n* is related to the amount of processes in the system. You can assume n<1000.
*	Id numbers of processes are lying in the range of int, and positive.
*	Take into consideration that there might be several processes in the system with the same priority at the same time.
	Priority is a whole positive number. The more urgent the process, the higher its priority.
*	You can assume that only one scheduler is running at the time.
*	You should also correctly deal with incorrect input: i.e. id number doesn't exist, or priority is a negative number, etc. In this case,
	the system should print error message that fits and do not make changes to the data structure.

### Class Diagram
![uml class diagram](https://raw.github.com/bolshchikov/scheduler-system/master/class_diagram.jpg)

### Implement
You should implement the methods descirbed below with the given complexity. Your implementation will be in `Scheduler.py`.
Explanations regarding the given files, in which hash tables and max heap are implemented, are provided further.

1.	**Scheduler()** - constructor. Complexity - *O(n)*.
2.	**void addProcess(int id, int priority)** - adds a new process to the system. Complexity - *O(lgn)*.
3.	**int scheduleByCreation()** - returns the id number of a process to be launched according to the time of creation. After this action, process recieves the processing time and leaves teh system. If the process doesn't end,
	it should be added to the system again.
	If there are no processes to schedule, `0` should be returned. Complexity - *O(1) the average + O(lgn)*.
4.	**int scheduleByPriority()** - returns the id number of a process to be launched according to the priority. After this action, process recieves the processing time and leaves teh system. If the process doesn't end,
	it should be added to the system again. If there are no processes to schedule, `0` should be returned. 
	Take into consideration, that system might posses several processes with the same priority.
	Complexity - *O(1) the average + O(lgn)*.
5.	**void changePriority(int d, int newPriority)** - changes the priroty of a process with given `id` to a `newPriority`. Complexity - *O(1) the average + O(lgn)*.
6.	**killProcess(int d)** - the process with a given `id` should be removed from a data structure, such that it won't be scheduled. Complexity - *O(1) the average + O(lgn)*.
7. 	**int numOfProcesses()** - returns the number of processes in a system. Complexity - *O(1)*.
8. 	**Scheduler()~** - destructor. Complexity - *O(n)*.

### Files
1.	`LinkedHash.py` - hash table with chaining to avoid collisions.
2. 	`MaxHeap.py` - max heap.
3.	`Process.py` - is almost given. The constructor should be implemented, and `equals` function.
4.	`example_output.py` - is the file for checks.

Your are allowed to write the extra code in file `schedule_extra.py`. 

***
[*The MIT License*](http://mit-license.org/)