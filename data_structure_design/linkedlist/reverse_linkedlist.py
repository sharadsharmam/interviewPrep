# def reverse_linkedlist(head: Node) -> Node:
#     if head is None:
#         return head
#     prev_node = None
#     curr_node = head
#     next_node = head.next
#     while next_node is not None:
#         curr_node.next = prev_node
#         prev_node = curr_node
#         curr_node = next_node
#         next_node = next_node.next
#     curr_node.next = prev_node
#     return curr_node

def reverse_linkedlist(head: Node, prev_node = None) -> Node:
    if head is None:
        return head
    elif head.next is None:
        head.next = prev_node
        return head
    next_node = head.next
    head.next = prev_node
    prev_node = head
    return reverse_linkedlist(next_node, head)