#https://oj.leetcode.com/problems/add-two-numbers/

'''You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

#Definition for singly-linked list.
#class ListNode:
#  def __init__(self, x):
#    self.val = x
#    self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
    res = None
    temp = res
    tens = 0
    while (l1!=None)or(l2!=None)or(tens!=0):
      val = ((l1.val if l1!=None else 0)+(l2.val if l2!=None else 0))+tens
      tens = val/10
      val = val%10
      if temp==None:
        res = ListNode(val)
        temp = res
      else:
        temp.next = ListNode(val)
        temp = temp.next
      l1 = l1.next if l1!=None else None
      l2 = l2.next if l2!=None else None
    return res
    
