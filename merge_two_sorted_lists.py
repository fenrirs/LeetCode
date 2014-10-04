#https://oj.leetcode.com/problems/merge-two-sorted-lists/

'''Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        tail = res
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        for node in (l1,l2):
            if node!=None:
                tail.next = node
        return res.next
