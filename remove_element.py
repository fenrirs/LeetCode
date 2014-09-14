#https://oj.leetcode.com/problems/remove-element/

'''Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        res = 0
        for i,x in enumerate(A):
            if x!=elem:
                A[res] = x
                res += 1
        A = A[:res]
        return res
