from ispalindrome import *
from linkedList import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = MyLinkedList()
    list1.addAtHead(1)
    list1.addAtTail(0)
    list1.addAtTail(1)
    # list1.printList()
    # print(list1.get(4))
    # list1.addAtIndex(0, 5)
    # list1.printList()
    # list1.deleteAtIndex(5)
    list1.printList()
    print(isPalindrome(list1.head))
