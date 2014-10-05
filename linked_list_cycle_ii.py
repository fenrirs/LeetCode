#https://oj.leetcode.com/problems/linked-list-cycle-ii/

'''Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        res = ListNode(0)
        res.next = head
        p1 = res
        p2 = res
        while p2!=None and p2.next!=None:
            p1 = p1.next
            p2 = p2.next.next
            if p1==p2:
                break
        if not p2 or not p2.next:
            return None
        p1 = res
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1
