# This is time_complexity = O(n) and space_complexity = O(n)
from linkedList import *


def isPalindrome(head: Node):
    linkedlist_len = 0
    list1 = []
    if head is None:
        return False
    curr_node = head
    while curr_node is not None:
        linkedlist_len += 1
        list1.append(curr_node.val)
        curr_node = curr_node.right
    # print(list1)
    # print(linkedlist_len)

    if linkedlist_len % 2 == 0:
        first_half = list1[:int(linkedlist_len / 2)]
        second_half = list1[int(linkedlist_len / 2):]
    else:
        first_half = list1[:int(linkedlist_len / 2)]
        second_half = list1[int(linkedlist_len / 2) + 1:]

    second_half.reverse()
    # print(first_half)
    # print(second_half)
    if first_half == second_half:
        return True
    else:
        return False
