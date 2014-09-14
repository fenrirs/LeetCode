#https://oj.leetcode.com/problems/divide-two-integers/

'''Divide two integers without using multiplication, division and mod operator.'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        res = 0
        fac = 0
        isNeg = (-1 if dividend<0 else 1)*(-1 if divisor<0 else 1)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend>>fac>divisor:
            fac += 1
        while dividend>=divisor:
            if dividend>=divisor<<fac:
                res += 1<<fac
                dividend -= divisor<<fac
            fac -= 1
        if isNeg==-1:
           # TO FOLLOW C RULES
           # if dividend>0:
           #     res += 1
            res = -res
        return res
