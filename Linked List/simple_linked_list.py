# Class for indivisual node
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

# Class for LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        # When linkedlist is blank
        if self.head is None:
            self.head = Node(data,None)
            return
        # When linkedlist is not blank
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data,None)

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def printLinkedList(self):
        print("\n")
        if self.head is None:
            print("Linked list is empty")
            return
        curr = self.head
        while curr:
            print(curr.data,end='-->')
            curr = curr.next

    # insert all values in one go
    def insert_values(self,data_list):
        self.head = None
        for i in range(len(data_list)):
            self.insert_at_end(data_list[i])

    # return the length of linked list
    def get_length(self):
        if self.head is None:
            print("Zero")

        cnt = 0
        curr = self.head
        while curr:
            curr = curr.next
            cnt +=1
        return cnt

    def remove(self,index):
        if index < 0 or index >= self.get_length():
            print("\n",index, "th index node is not present in linked list")
            return

        # Removing Head
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1

    def insert_at_index(self,index,data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return

        curr = self.head
        count = 0
        while curr:
            if count == index - 1:
                node = Node(data,curr.next)
                curr.next = node
                return
            curr = curr.next
            count += 1

if __name__ =='__main__':
    l1 = LinkedList()
    l1.insert_at_end(10)
    l1.insert_at_end(20)
    l1.insert_at_end(30)

    l1.insert_at_beginning(100)

    # Inserting all the values at one go
    data_list = ["Pallavi","Akhil","Pravin","Nitin","Mummy","Pappa"]
    l1.insert_values(data_list)

    l1.printLinkedList()

    # Returns the length of linked list
    print("\n Length of linked list is ",l1.get_length())

    # Removes the node from specified index
    l1.remove(1)
    l1.remove(10)
    l1.printLinkedList()
    l1.remove(4)
    l1.printLinkedList()

    l1.insert_at_index(2,"Bonakruti")
    l1.printLinkedList()
