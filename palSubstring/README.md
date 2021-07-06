# Longest Palindrome Substring

$ python main.py <br/>
<br/>
{'a': [0, 2], 'b': [1], 'x': [3, 8], 'y': [4, 7], 'z': [5, 6], 'f': [9], 'g': [10, 11]} <br/>
<br/>
key: a, list: [0, 2] <br/>
<br/>
listNode gap: 2 <br/>
self.head == None <br/>
gap: 2 <br/>
<br/>
key: b, list: [1] <br/>
<br/>
listNode gap: 0 <br/>
<br/>
currPtr.dataNode.gap >= listNode.dataNode.gap and currPtr.next == None <br/>
prevPtr.gap: 2, currPtr.gap: 2, listNode.dataNode.gap: 0 <br/>
gap: 2 <br/>
gap: 0 <br/>
<br/>
key: x, list: [3, 8] <br/>
<br/>
listNode gap: 5 <br/>
<br/>
listNode.dataNode.gap >= self.head.dataNode.gap <br/>
gap: 5 <br/>
gap: 2 <br/>
gap: 0 <br/>
<br/>
key: y, list: [4, 7] <br/>
<br/>
listNode gap: 3 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 3 <br/>
<br/>
prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap <br/>
prevPtr.gap: 5, currPtr.gap: 2, listNode.dataNode.gap: 3 <br/>
gap: 5 <br/>
gap: 3 <br/>
gap: 2 <br/>
gap: 0 <br/>
<br/>
key: z, list: [5, 6] <br/>
<br/>
listNode gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 1 <br/>
<br/>
prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap <br/>
prevPtr.gap: 2, currPtr.gap: 0, listNode.dataNode.gap: 1 <br/>
gap: 5 <br/>
gap: 3 <br/>
gap: 2 <br/>
gap: 1 <br/>
gap: 0 <br/>
<br/>
key: f, list: [9] <br/>
<br/>
listNode gap: 0 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 0 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 0 <br/>
<br/>
else <br/>
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 0 <br/>
<br/>
else <br/>
prevPtr.gap: 2, currPtr.gap: 1, listNode.gap: 0 <br/>
<br/>
listNode.gap == currPtr.gap: == 0 <br/>
<br/>
prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap <br/>
prevPtr.gap: 1, currPtr.gap: 0, listNode.dataNode.gap: 0 <br/>
gap: 5 <br/>
gap: 3 <br/>
gap: 2 <br/>
gap: 1 <br/>
gap: 0 <br/>
gap: 0 <br/>
<br/>
key: g, list: [10, 11] <br/>
<br/>
listNode gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 5, listNode.gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 5, currPtr.gap: 3, listNode.gap: 1 <br/>
<br/>
else <br/>
prevPtr.gap: 3, currPtr.gap: 2, listNode.gap: 1 <br/>
<br/>
listNode.gap == currPtr.gap: == 1 <br/>
<br/>
prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap <br/>
prevPtr.gap: 2, currPtr.gap: 1, listNode.dataNode.gap: 1 <br/>
gap: 5 <br/>
gap: 3 <br/>
gap: 2 <br/>
gap: 1 <br/>
gap: 1 <br/>
gap: 0 <br/>
gap: 0 <br/>
<br/>
i: 3, j: 8 <br/>
Palindrome substring: xyzzyx <br/>
<br/>