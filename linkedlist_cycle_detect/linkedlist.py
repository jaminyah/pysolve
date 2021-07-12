from node import ListNode

class LinkedList:

    def __init__(self):
        self.head = None
   
    def getHead(self) -> ListNode:
        return self.head

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def setEmpty(self):
        self.head = None

    # Insert a new node at the head
    def addNodeHead(self, node: ListNode):
        
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # Insert a new node at the tail
    def addNodeTail(self, node: ListNode):

        if self.head is None:
            self.head = node
        else:
            nodePtr = self.head
            prevPtr = None
            while (nodePtr is not None):
                prevPtr = nodePtr
                nodePtr = nodePtr.next
            prevPtr.next = node

    # Delete node of a specific value
    def delNode(self, node: ListNode):
        nodePtr = self.head
        prevNode = ListNode()
    
        while (nodePtr.value is not node.value):
                prevNode = nodePtr
                nodePtr = nodePtr.next
        
        if nodePtr.next is None:
            prevNode.next = None
        else:
            nodePtr.value = nodePtr.next.value        
            nodePtr.next = nodePtr.next.next

        
    # Reverse list
    def reverseList(self, head: ListNode):
        prevNode = None
        currNode = self.head

        while (currNode is not None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        self.head = prevNode

    def showList(self):
        nodePtr = self.head

        while (nodePtr is not None):
            print(f"{nodePtr.value}, ")
            nodePtr = nodePtr.next