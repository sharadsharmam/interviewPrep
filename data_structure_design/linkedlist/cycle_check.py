from linkedList import *

# This solution has a time complexity of O(n) and space complexity of O(n)
# def hasCycle(self, head: Node) -> bool:
#     if head is None or head.next is None:
#         return False
#     hash_set = set([])
#     curr_node = head
#     while curr_node:
#         if curr_node in hash_set:
#             return True
#         hash_set.add(curr_node)
#         curr_node = curr_node.next
#     return False

# This solution has a time complexity of O(n) and space complexity of O(1)
def hasCycle(self, head: Node) -> bool:
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next
    while fast.next and fast.next.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
