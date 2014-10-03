#https://oj.leetcode.com/problems/reorder-list/

'''Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reverseList(self,head):
        if not head or not head.next:
            return head
        pPre = None
        pTemp = head
        pNext = head.next
        while pNext!=None:
            pTemp.next = pPre
            pPre = pTemp
            pTemp = pNext
            pNext = pNext.next
        pTemp.next = pPre
        return pTemp
        
    def reorderList(self, head):
        if not head or not head.next:
        	return head
        res = ListNode(0)
        res.next = head
        part1 = res
        part2 = res
        while part2.next!=None and part2.next.next!=None:
            part1 = part1.next
            part2 = part2.next.next
        part2 = part1.next
        part1.next = None
        part2 = self.reverseList(part2)
        part1 = head
        while part1!=None:
            p1Next = part1.next
            part1.next = part2
            p2Next = part2.next
            if p1Next!=None:
                part2.next = p1Next
            else:
                part2.next = p2Next
                break
            part1 = p1Next
            part2 = p2Next
        return res.next
