# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def printNode(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(10)
    second = Node(20)
    third = Node(30)
    llist.head.next = second
    second.next = third
    third.next = None

    llist.printNode()
