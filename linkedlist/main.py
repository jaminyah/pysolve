# Leetcode: #206

from linkedlist import LinkedList
from node import ListNode

linked = LinkedList()
head = linked.addNodeHead(8)
head = linked.addNodeHead(7)
head = linked.addNodeHead(6)
head = linked.addNodeHead(5)
head = linked.addNodeHead(9)
linked.showList()

linked.reverseList(head)
node = ListNode(5)
linked.delNode(node)
linked.showList()