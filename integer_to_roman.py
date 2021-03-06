#https://oj.leetcode.com/problems/integer-to-roman/

'''Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'), (50,'L'),
                (90,'XC'), (100,'C'), (400,'CD'), (500,'D'), (900,'CM'), (1000,'M')]
        
        res = ''
        p = len(roman)-1
        while p>=0:
            if num>=roman[p][0]:
                res += roman[p][1]
                num -= roman[p][0]
            else:
                p -= 1
        return res
