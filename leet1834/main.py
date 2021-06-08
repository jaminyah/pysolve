# Solution to Leetcode: 1834 - Single threaded CPU
# Author - Patrick Allison
# Date - June 7, 2021

from pqueue import PriorityQueue
from typing import List

def getOrder(tasks: List[List[int]]) -> List[int]:

    print(f"Initial tasks: {tasks}")
    tasks.sort()                                                # Sort ascending enqueueTime
    print(f"After sort: {tasks}")

    cpuTasks: List[int] = []                                    # List of task processed by CPU
    pq = PriorityQueue()                                        # Data structure
    cpuTime = 1                                               # Total CPU run-time
    enqueueTime = 0
    processTime = 0

    i = 0                                                       # First task in the remaining task list
    while len(tasks) > 0:

        task = tasks[i]
        print(f"task:    {task}")
        enqueueTime = task[0]                                   # task[enqueueTime, processingTime] - index 0 is enqueueTime
 
        if enqueueTime <= cpuTime:  
            
            pq.insert(task)                                     
            print(f"Priority Queue: {pq}")

            del tasks[0]                                        # Task is added to the Q so remove from task list
            print(f"Task list: {tasks}")
            continue
        elif pq.isEmpty() == True:
            cpuTime = cpuTime + 1
            print(f"cpuTime: {cpuTime}")
        else:
            print(f"\npq.isEmpty: {pq.isEmpty()}")
            cpuTask = pq.getPriority()
            cpuTasks.append(cpuTask)                            # List for returning order of tasks run by the CPU

            print(f"cpu - [{cpuTask[0]}, {cpuTask[1]}]")
            processingTime = cpuTask[1]                         # cpuTask[enqueueTime, processingTime] - index 1 is processingTime
            while processingTime != 0:
                processingTime = processingTime - 1
                cpuTime = cpuTime + 1
                print(f"cpuTime: {cpuTime}")

    while pq.isEmpty() != True:
        print(f"\npq.isEmpty: {pq.isEmpty()}")
        cpuTask = pq.getPriority()
        cpuTasks.append(cpuTask)                                # List for returning order of tasks run by the CPU

        print(f"cpu - [{cpuTask[0]}, {cpuTask[1]}]")
        processingTime = cpuTask[1]                             # cpuTask[enqueueTime, processingTime] - index 1 is processingTime
        while processingTime != 0:
            processingTime = processingTime - 1
            cpuTime = cpuTime + 1
            print(f"cpuTime: {cpuTime}")

    return cpuTasks

if __name__ == '__main__':
    tasklist = [[1, 2], [2, 4], [3, 2], [4, 1]]
    #tasklist = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    cpuTasklist = getOrder(tasklist)
    print(f"Task run order: {cpuTasklist}")
