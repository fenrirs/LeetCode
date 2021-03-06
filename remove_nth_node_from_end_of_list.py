#https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

'''Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
   
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head==None:
            return None
        head1 = ListNode(0)
        head1.next = head
        p1 = head1
        p2 = head1
        for i in range(n):
            p2 = p2.next
        while p2.next!=None:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return head1.next
