from linkedList import *

# Solution with time complexity O(m+n) and space complexity O(1) but the node.val should be > 0 otherwise this
# method won't work.

# def getIntersectionNode(headA: Node, headB: Node):
#     if headA is None or headB is None:
#         return None
#     list1_node = headA
#     while list1_node:
#         list1_node.val = list1_node.val * -1
#         list1_node = list1_node.next
#
#     list2_node = headB
#     intersecting_node = None
#     while list2_node:
#         if list2_node.val < 0:
#             intersecting_node = list2_node
#             break
#         list2_node = list2_node.next
#
#     list1_node = headA
#     while list1_node:
#         list1_node.val = list1_node.val * -1
#         list1_node = list1_node.next
#
#     return intersecting_node



# Solution with time complexity O(m+n) and space complexity O(1)

def getIntersectionNode(headA: Node, headB: Node):
    if headA is None or headB is None:
        return None
    list1_node = headA
    list1_length = 1
    while list1_node:
        list1_length += 1
        list1_node = list1_node.next

    list2_node = headB
    list2_length = 1
    while list2_node:
        list2_length += 1
        list2_node = list2_node.next

    list_length_diff = abs(list1_length - list2_length)
    list1_node = headA
    list2_node = headB
    if list_length_diff > 0 and list1_length > list2_length:
        while list_length_diff != 0:
            list1_node = list1_node.next
            list_length_diff -= 1
    elif list_length_diff > 0 and list2_length > list1_length:
        while list_length_diff != 0:
            list2_node = list2_node.next
            list_length_diff -= 1
    intersecting_node = None
    while list1_node and list2_node:
        if list1_node == list2_node:
            intersecting_node = list1_node
            break
        list1_node = list1_node.next
        list2_node = list2_node.next
    return intersecting_node
