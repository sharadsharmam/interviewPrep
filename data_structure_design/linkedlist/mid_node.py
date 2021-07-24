from linkedList import *

def middleNode(head: Node):
    if head is None:
        return False
    curr_node = head
    mid_node = head
    length = 1
    while curr_node:
        length += 1
        curr_node = curr_node.next
        if length % 2 != 0:
            mid_node = mid_node.next
    return mid_node