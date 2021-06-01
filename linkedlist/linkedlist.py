from node import ListNode

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def setEmpty(self) -> ListNode:
        self.head = None
        return self.head

    # Insert a new node at the head
    def addNodeHead(self, value) -> ListNode:
        node = ListNode(value)
        node.next = self.head
        self.head = node
        return self.head

    # Insert a new node at the tail
    def addNodeTail(self, value):
        node = ListNode(value)

        if self.head is None:
            self.head = node
        else:
            tempNode = self.head
            while (tempNode is not None):
                tempNode = tempNode.next
            tempNode.next = node

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
    def reverseList(self, head: ListNode) -> ListNode:
        prevNode = None
        currNode = self.head

        while (currNode is not None):
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        self.head = prevNode
        return head

    def showList(self):
        node = self.head
        list = []

        while (node is not None):
            list.append(node.value)
            node = node.next
        print(list)