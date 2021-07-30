# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        #print(head,left,right)
        prev = None
        curr = head
        next = None
        if left <= right:
            while head:
                if head.val == left:
                    curr = head
                    while curr:
                        next = curr.next
                        curr.next = prev
                        prev = curr
                        curr = next
                    return prev
                else:
                    head = head.next
        else:
            return head

    def printList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)

s = Solution()
rev = s.reverseBetween(head,2,4)
s.printList(rev)
