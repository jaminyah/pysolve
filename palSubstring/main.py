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

    def isPalindrome(self, string: str) -> bool:

        i = 0
        j = len(string) - 1
        input = string.lower()

        while (i <= j):
            if input[i] == input[j]:
                i = i + 1
                j = j - 1
            else:
                return False
        return True
    

    def getLongestPalindrome(self, head: ListNode, string: str) -> str:

        longest = ""
        if len(string) == 1:
            longest = string
            return longest
 
        nodePtr = head
        while nodePtr != None:
            indices = nodePtr.dataNode.indices
            last = len(indices)

            k = indices[0]
            l = indices[last - 1]   
            l = l + 1                          # handle slice operation
            print(f"k: {k}, l: {l}")
            subString = string[k:l]
            if self.isPalindrome(subString) == True:
                if len(subString) > len(longest):
                    longest = subString
                    #return longest
            else:
                for i in range(1, l):
                    print(f"i: {i}, l: {l}")
                    subString = string[i:l]
                    if self.isPalindrome(subString) == True:
                        if len(subString) > len(longest):
                            longest = subString
                            #return longest

            # loop thru the remaining indices
            for i in range(last - 1):
                j = i + 1
                m = indices[i]
                n = indices[j]
                print(f"i: {m}, j: {n}")

                n = n + 1                    # slice operation stops at j - 1
                subString = string[m:n]  
                print(f"subString: {subString}")

                if self.isPalindrome(subString) == True:
                    if len(subString) > len(longest):
                        longest = subString
                    else:
                        subString = ""

            nodePtr = nodePtr.next

        return longest

"""
if __name__ == '__main__':
    input = "ccabcaaaabbccccccc"
    soln = Solution()
    table = soln.buildHashTable(input)
    head = soln.buildSortedListNodes(table)
    result = soln.getLongestPalindrome(head, input)
    print(result)
"""