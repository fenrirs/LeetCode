#https://oj.leetcode.com/problems/merge-k-sorted-lists/

'''Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        lists = filter(None,lists)
        res = ListNode(0)
        tail = res
        while len(lists)>0:
            lists.sort(key=lambda l:l.val)
            tail.next = lists[0]
            tail = tail.next
            lists[0] = lists[0].next
            #optimize
            if lists[0]==None:
                p = 1
                while p<len(lists):
                    tail.next = lists[p]
                    #print lists[p].val
                    tail = tail.next
                    lists[p] = lists[p].next
                    if lists[p]==None:
                        p += 1
                    else:
                        break
                lists = lists[p:]
        return res.next
