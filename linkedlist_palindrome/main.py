from linkedlist import LinkedList 
from linkedlist import ListNode

def isPalindrome(head: ListNode) -> bool:
    
    # count total number of nodes
    numNodes = 0
    nextPtr = head
    while (nextPtr != None):
        numNodes += 1
        nextPtr = nextPtr.next
    nextPtr = None

    if numNodes == 1:
        return True
 
    prevPtr = head
    nextPtr = head.next
    prevPtr.next = None
    oddCount = False

    if numNodes % 2 == 0:
        mid = numNodes // 2                 # floor division operator
    else:
        mid = (numNodes - 1) // 2
        oddCount = True

    # reverse left nodes up to midpoint
    count = 0
    while nextPtr != None:
        count += 1
        if count < mid:
            head = nextPtr
            nextPtr = nextPtr.next
            head.next = prevPtr
            prevPtr = head
        else:
            break

    if oddCount == True:
        nextPtr = nextPtr.next      # set right count == left count

    # Palindrome check
    while head != None and nextPtr != None:
        print(f"{head.value}, {nextPtr.value}")

        if head.value == nextPtr.value:
            head = head.next
            nextPtr = nextPtr.next
        else:
            return False
    return True

if __name__ == '__main__':

    node0 = ListNode('a')
    node1 = ListNode('b')
    node2 = ListNode('c')
    node3 = ListNode('d')
    node4 = ListNode('e')
    node5 = ListNode('e')
    node6 = ListNode('d')
    node7 = ListNode('c')
    node8 = ListNode('b')
    node9 = ListNode('a')
    midNode = ListNode('f')

    ll = LinkedList()

    ll.addNodeTail(node0)
    ll.addNodeTail(node1)
    ll.addNodeTail(node2)
    ll.addNodeTail(node3)
    ll.addNodeTail(node4)
    ll.addNodeTail(midNode)
    ll.addNodeTail(node5)
    ll.addNodeTail(node6)
    ll.addNodeTail(node7)
    ll.addNodeTail(node8)
    ll.addNodeTail(node9)
    
    headPtr = ll.getHead()

    result = isPalindrome(headPtr)
    print(f"isPalindrome: {result}")    