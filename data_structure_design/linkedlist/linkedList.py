class Node:
    def __init__(self, val):
        self.val = val
        self.right = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val: int):
        temp_node = self.head
        self.head = Node(val)
        self.head.right = temp_node

    def addAtTail(self, val: int):
        if self.head is None:
            self.head = Node(val)
            self.head.right = None
            return
        curr_node = self.head
        while curr_node.right is not None:
            curr_node = curr_node.right
        curr_node.right = Node(val)
        curr_node.right.right = None

    def get(self, index: int):
        if index < 0 or self.head is None:
            return -1
        curr_node = self.head
        while index > 0:
            if curr_node.right is None:
                return -1
            curr_node = curr_node.right
            index -= 1

        return curr_node.val

    def printList(self):
        if self.head == None:
            print("Linked list is empty")
        curr_node = self.head
        while curr_node != None:
            if curr_node.right is None:
                print(f"{curr_node.val} -> None")
            else:
                print(f"{curr_node.val} -> ", end='')
            curr_node = curr_node.right

    def addAtIndex(self, index: int, val: int):
        if index < 0 or (self.head is None and index > 0):
            return
        if index == 0:
            next_node = Node(val)
            next_node.right = self.head
            self.head = next_node
        else:
            curr_node = self.head
            while index-1 > 0:
                if curr_node.right is None:
                    return
                curr_node = curr_node.right
                index -= 1
            next_node = Node(val)
            if curr_node.right is None:
                next_node.right = None
            else:
                next_node.right = curr_node.right
            curr_node.right = next_node

    def deleteAtIndex(self, index: int):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.right
        else:
            curr_node = self.head
            while index-1 > 0:
                if curr_node.right is None:
                    return
                curr_node = curr_node.right
                index -= 1
            if curr_node.right is None:
                return
            curr_node.right = curr_node.right.right
