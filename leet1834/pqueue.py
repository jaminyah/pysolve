# Reference: https://www.geeksforgeeks.org/priority-queue-in-python/

from typing import List

class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def dequeueMax(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def getPriority(self):                                  # For List[List[int]] - Leetcode # 1834
        try:
            min = 0                                         # minimum index
            minProcessTime = self.queue[min][1]
            for i in range(len(self.queue)):
                task = self.queue[i]
                if task[1] < minProcessTime:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

    def dequeueMin(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(12)
    pq.insert(1)
    pq.insert(14)
    pq.insert(7)

    print(pq)
    while not pq.isEmpty():
        pq.dequeueSM()
        print(pq)    