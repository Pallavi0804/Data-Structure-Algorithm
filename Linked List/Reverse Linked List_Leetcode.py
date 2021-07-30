# https://leetcode.com/problems/reverse-linked-list/
# https://www.youtube.com/watch?v=gSs3U18v4xE
# Steps
# 1. Set Previous as None, Current as head and next as None
# 2. Iterate until current is None
# 3. set next node of current to previous
# 4. set previous as current, current as next
# 5. head points to the next node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def printList(self,head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

n5 = ListNode(5,None)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
head = ListNode(1,n2)

s = Solution()
rev = s.reverseList(head)
s.printList(rev)



