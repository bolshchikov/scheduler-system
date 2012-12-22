import Scheduler

def main():
    print 'Running the example main.\n'
    scheduler = Scheduler.Scheduler()
    print '1. There are %d processes in the system\n' % scheduler.numOfProcesses()
    scheduler.addProcess(345,34)
    scheduler.addProcess(347,78)
    scheduler.addProcess(457,10)
    scheduler.addProcess(789,4567)
    scheduler.addProcess(34,3)
    scheduler.addProcess(47,25)
    scheduler.addProcess(2457,109)
    scheduler.addProcess(89,45)
    scheduler.addProcess(5,3004)

    print '2. Now there are %d  processes in the syste' % scheduler.numOfProcesses()
    print '3. First one scheduled by creation is ID: %d' % scheduler.scheduleByCreation()
    print '4. Second one scheduled by priority is ID: %d' % scheduler.scheduleByPriority()
    print '5. Now there are %d processes in the system' % scheduler.numOfProcesses()

    scheduler.changePriority(457,6666)
    print '6. Third one scheduled by priority is ID: %d' % scheduler.scheduleByPriority()
    print '7. Forth one scheduled by creation is ID: %d' % scheduler.scheduleByCreation()
    print '8. Fifth one scheduled by priority is ID: %d' % scheduler.scheduleByPriority()
  
    print '9. Now there are %d processes in the system' % scheduler.numOfProcesses()

    scheduler.changePriority(34,6666)
    print '10. Sixth one scheduled by priority is ID: %d' % scheduler.scheduleByPriority()
    
    scheduler.changePriority(47,26)
    scheduler.changePriority(47,27)
    scheduler.changePriority(47,3)
    print '11. Now there are %d processes in the system' % scheduler.numOfProcesses()
    scheduler.addProcess(345,3004)
    scheduler.addProcess(346,344)
    print '12. After adding 2 processes, there are %d processes in the syste' % scheduler.numOfProcesses()
    print '13. Seventh one scheduled by creation is ID: %d' % scheduler.scheduleByCreation()
    print '14. Eighth one scheduled by priority is ID: %d' % scheduler.scheduleByPriority()
    scheduler.killProcess(3004)
    scheduler.killProcess(346)
    print '15. Ninth one scheduled by priority is ID: %d'  % scheduler.scheduleByPriority()
    
    scheduler.destroy()
    print '\n\n' 
    return 0

if __name__=='__main__':
    main()