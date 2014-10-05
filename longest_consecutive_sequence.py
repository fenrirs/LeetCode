#https://oj.leetcode.com/problems/longest-consecutive-sequence/

'''Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {}
        res = 0
        for i,x in enumerate(num):
            dict[x] = True
        for i,x in enumerate(num):
            if not x in dict:
            	continue
            del dict[x]
            p1,p2 = x,x
            while p1-1 in dict:
                p1 -= 1
                del dict[p1]
            while p2+1 in dict:
                p2 += 1
                del dict[p2]
            res = max(res,p2-p1+1)
        return res
