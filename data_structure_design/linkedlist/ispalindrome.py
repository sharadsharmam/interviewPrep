from linkedList import *


# This solution has time_complexity = O(n) and space_complexity = O(n)
#######################################################################################################################
# def isPalindrome(head: Node) -> bool:
#     linkedlist_len = 0
#     list1 = []
#     if head is None:
#         return False
#     curr_node = head
#     while curr_node is not None:
#         linkedlist_len += 1
#         list1.append(curr_node.val)
#         curr_node = curr_node.right
#     # print(list1)
#     # print(linkedlist_len)
#
#     if linkedlist_len % 2 == 0:
#         first_half = list1[:int(linkedlist_len / 2)]
#         second_half = list1[int(linkedlist_len / 2):]
#     else:
#         first_half = list1[:int(linkedlist_len / 2)]
#         second_half = list1[int(linkedlist_len / 2) + 1:]
#
#     second_half.reverse()
#     # print(first_half)
#     # print(second_half)
#     if first_half == second_half:
#         return True
#     else:
#         return False
#######################################################################################################################


# This solution has time_complexity = O(n) and space_complexity = O(1)
#######################################################################################################################
def reverse_linkedlist(head: Node) -> Node:
    if head is None:
        return head
    prev_node = None
    curr_node = head
    next_node = head.right
    while next_node is not None:
        curr_node.right = prev_node
        prev_node = curr_node
        curr_node = next_node
        next_node = next_node.right
    curr_node.right = prev_node
    return curr_node



def isPalindrome(head: Node) -> bool:
    if head is None:
        return False
    curr_node = head
    mid_node = head
    length = 1
    while curr_node.right:
        length += 1
        curr_node = curr_node.right
        if length % 2 != 0:
            mid_node = mid_node.right
    # print(f"length = {length}")

    temp_node_1 = head
    temp_node_2 = reverse_linkedlist(mid_node)
    while temp_node_1 and temp_node_2:
        # print(f"temp_node_1.val = {temp_node_1.val}")
        # print(f"temp_node_2.val = {temp_node_2.val}")
        if temp_node_1.val != temp_node_2.val:
            return False
        temp_node_1 = temp_node_1.right
        temp_node_2 = temp_node_2.right
    if length % 2 == 0:
        return (temp_node_2 == mid_node) and (temp_node_1 is None)
    else:
        return (temp_node_1 is None) and (temp_node_2 is None)
#######################################################################################################################
