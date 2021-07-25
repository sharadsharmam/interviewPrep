from linkedList import *

def deleteDuplicates(self, head: Node) -> Node:
    if head is None or head.next is None:
        return head
    curr_node = head
    while curr_node:
        temp_node = curr_node
        while curr_node and curr_node.val <= temp_node.val:
            curr_node = curr_node.next
        temp_node.next = curr_node
    return head