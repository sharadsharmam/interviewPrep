from linkedList import Node

class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return

    def pop(self) -> None:
        if self.head is None:
            return
        self.head = self.head.next
        return

    def top(self) -> int:
        if self.head is None:
            return
        return self.head.val

    def getMin(self) -> int:
        if self.head is None:
            return
        min_val = self.head.val
        curr_node = self.head.next
        while curr_node:
            if curr_node.val < min_val:
                min_val = curr_node.val
            curr_node = curr_node.next
        return min_val
