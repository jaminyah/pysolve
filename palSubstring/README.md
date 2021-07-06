# Longest Palindrome Substring

$ python main.py
{'a': [0, 2], 'b': [1], 'x': [3, 8], 'y': [4, 7], 'z': [5, 6], 'f': [9], 'g': [10, 11]}

key: a, list: [0, 2]

listNode gap: 2
self.head == None
gap: 2

key: b, list: [1]

listNode gap: 0

currPtr.dataNode.gap >= listNode.dataNode.gap and currPtr.next == None
prevPtr.gap: 2, currPtr.gap: 2, listNode.dataNode.gap: 0
gap: 2
gap: 0

key: x, list: [3, 8]

listNode gap: 5

listNode.dataNode.gap >= self.head.dataNode.gap
gap: 5
gap: 2
gap: 0

key: y, list: [4, 7]

listNode gap: 3

else
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 3

prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap
prevPtr.gap: 5, currPtr.gap: 2, listNode.dataNode.gap: 3
gap: 5
gap: 3
gap: 2
gap: 0

key: z, list: [5, 6]

listNode gap: 1

else
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 1

else
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 1

else
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 1

prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap
prevPtr.gap: 2, currPtr.gap: 0, listNode.dataNode.gap: 1
gap: 5
gap: 3
gap: 2
gap: 1
gap: 0

key: f, list: [9]

listNode gap: 0

else
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 0

else
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 0

else
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 0

else
prevPtr.gap: 2, currPtr.gap: 1, listNode.gap: 0

listNode.gap == currPtr.gap: == 0

prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap
prevPtr.gap: 1, currPtr.gap: 0, listNode.dataNode.gap: 0
gap: 5
gap: 3
gap: 2
gap: 1
gap: 0
gap: 0

key: g, list: [10, 11]

listNode gap: 1

else
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 1

else
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 1

else
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 1

listNode.gap == currPtr.gap: == 1

prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap
prevPtr.gap: 2, currPtr.gap: 1, listNode.dataNode.gap: 1
gap: 5
gap: 3
gap: 2
gap: 1
gap: 1
gap: 0
gap: 0
i: 3, j: 8
Palindrome substring: xyzzyx