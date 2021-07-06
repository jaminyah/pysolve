from typing import List

class DataNode:
    def __init__(self, key: str, gap: int, indices: List[int]):
        self.key = key
        self.gap = gap                          # indices[first] - indices[last]
        self.indices = indices

class ListNode:
    def __init__(self, dataNode: DataNode):
        self.dataNode = dataNode
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    # Insert a new node at the head
    def addNode(self, dataNode: DataNode) -> ListNode:

        listNode = ListNode(dataNode)

        if self.head == None:
            self.head = listNode
        else:
            listNode.next = self.head
            self.head = listNode
        return self.head
    
    # Insert a new node in sorted position
    def addNodeSorted(self, dataNode: DataNode) -> ListNode:

        listNode = ListNode(dataNode)
        print(f"\nlistNode gap: {listNode.dataNode.gap}")

        if self.head == None:
            print("self.head == None")
            self.head = listNode
        else:
            currPtr = self.head
            prevPtr = self.head
            while currPtr != None:

                # DEBUG
                if listNode.dataNode.gap == currPtr.dataNode.gap:
                    print(f"\nlistNode.gap == currPtr.gap: == {listNode.dataNode.gap}")

                if listNode.dataNode.gap >= self.head.dataNode.gap:
                    print("\nlistNode.dataNode.gap >= self.head.dataNode.gap")
                    listNode.next = self.head
                    self.head = listNode
                    break

                elif prevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap:
                    print("\nprevPtr.dataNode.gap > listNode.dataNode.gap and listNode.dataNode.gap >= currPtr.dataNode.gap")
                    print(f"prevPtr.gap: {prevPtr.dataNode.gap}, currPtr.gap: {currPtr.dataNode.gap}, listNode.dataNode.gap: {listNode.dataNode.gap}")
                    prevPtr.next = listNode
                    listNode.next = currPtr
                    break

                elif currPtr.dataNode.gap >= listNode.dataNode.gap and currPtr.next == None:
                    print("\ncurrPtr.dataNode.gap >= listNode.dataNode.gap and currPtr.next == None")
                    print(f"prevPtr.gap: {prevPtr.dataNode.gap}, currPtr.gap: {currPtr.dataNode.gap}, listNode.dataNode.gap: {listNode.dataNode.gap}")
                    currPtr.next = listNode
                    listNode.next = None
                    break

                else:
                    print("\nelse")
                    print(f"prevPtr.gap: {prevPtr.dataNode.gap}, currPtr.gap: {currPtr.dataNode.gap}, listNode.gap: {listNode.dataNode.gap}")
                    prevPtr = currPtr
                    currPtr = currPtr.next
        return self.head

    def showNodes(self, head: ListNode):

        nodePtr = head
        while nodePtr != None:
            print(f"gap: {nodePtr.dataNode.gap}")
            nodePtr = nodePtr.next

class Solution:
    def buildHashTable(self, array: str) -> dict:

        length = len(array)
        hashTable = dict()

        # count occurrence of each array item
        for index, key in enumerate(array):
            hashTable.setdefault(key, []).append(index)

        return hashTable

    def buildSortedListNodes(self, hTable: dict) -> ListNode:

        linkedList = LinkedList()
 
        for k, v in hTable.items():
            print(f"\nkey: {k}, list: {v}")

            key = k
            indexes = v

            first = indexes[0]
            length = len(indexes) - 1
            last = indexes[length]
            gap = last - first

            dataNode = DataNode(key, gap, indexes)
            headNode = linkedList.addNodeSorted(dataNode)
            linkedList.showNodes(headNode)

        return headNode

    def isPalindrome(self, input: str) -> bool:
        reversed = input[::-1]
        if input == reversed:
            return True
        else:
            return False

    def getLongestPalindrome(self, head: ListNode, string: str) -> str:

        subString = ""
        nodePtr = head

        while nodePtr != None:
            indices = nodePtr.dataNode.indices
            i = indices[0]
            length = len(indices) - 1
            j = indices[length]
            print(f"i: {i}, j: {j}")

            j = j + 1                           # slice operation stops at j - 1
            subString = string[i:j]  
            if self.isPalindrome(subString) == True:
                break
            else:
                subString = ""
                nodePtr = nodePtr.next
        
        return subString

 
if __name__ == '__main__':
    input = "abaxyzzyxfgg"
    soln = Solution()
    table = soln.buildHashTable(input)
    print(table)

    head = soln.buildSortedListNodes(table)
    result = soln.getLongestPalindrome(head, input)
    print(f"Palindrome substring: {result}")
