#https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

'''Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def checkK(self,head,k):
        for i in range(k):
            head = head.next
            if head==None:
                return False
        return True
        
    def reverseKGroup(self, head, k):
        if k<2:
            return head
        res = ListNode(0)
        res.next = head
        res1 = res
        while self.checkK(res1,k):
            nextRes1 = res1.next
            qPre = res1.next
            qTemp = qPre.next
            qNext = qTemp.next
            for i in range(k-2):
                qTemp.next = qPre
                qPre = qTemp
                qTemp = qNext
                qNext = qNext.next
            qTemp.next = qPre
            res1.next = qTemp
            nextRes1.next = qNext
            res1 = nextRes1
        return res.next
        
if __name__=='__main__':
	s = Solution()

	l1 = ListNode(1)
	l2 = ListNode(2)
	l3 = ListNode(3)
	l4 = ListNode(4)
	l5 = ListNode(5)
	l6 = ListNode(6)
	l1.next = l2
	l2.next = l3
	l3.next = l4
	l4.next = l5
	l5.next = l6

	root = s.reverseKGroup(l1,2)

	while root!=None:
		print root.val
		root = root.next
