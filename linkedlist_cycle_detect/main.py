from linkedlist import LinkedList 
from node import ListNode

def findLinkedCycle(head: ListNode) -> ListNode:
    slowPtr = head
    fastPtr = head

    # fast pointer speed = 2 x slow pointer speed
    while fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

        if slowPtr == fastPtr:
            print(f"loop1 - slowPtr == fastPtr: {slowPtr.value}")
            break
        else:
            print(f"loop1 - slowPtr: {slowPtr.value}, fastPtr: {fastPtr.value}")

    # fast pointer = first node. speed = slow pointer
    fastPtr = head
    while fastPtr:
        if slowPtr == fastPtr:
            print(f"loop2 - slowPtr: {slowPtr.value}, fastPtr: {fastPtr.value}")
            return slowPtr
        else:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
    
    return head

if __name__ == '__main__':

    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    ll = LinkedList()

    ll.addNodeTail(node0)
    ll.addNodeTail(node1)
    ll.addNodeTail(node2)
    ll.addNodeTail(node3)
    ll.addNodeTail(node4)
    ll.addNodeTail(node5)
    ll.addNodeTail(node6)
    ll.addNodeTail(node7)
    ll.addNodeTail(node8)
    ll.addNodeTail(node9)

    node9.next = node0

    head = ll.getHead()

    node = findLinkedCycle(head)
    print(f"Node value: {node.value}")

