#https://oj.leetcode.com/problems/reverse-integer/

'''Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution:
    # @return an integer
    def reverse(self, x):
        res = 0
        isNeg = False
        if x<0:
            isNeg = True
            x = -x
        while x!=0:
            res = res*10 + x%10
            x /= 10
        if isNeg:
            res = -res
        return res
        
