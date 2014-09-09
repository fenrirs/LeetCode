#https://oj.leetcode.com/problems/roman-to-integer/

'''Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        head = 0
        while head<len(s)-1:
            if roman[s[head]]<roman[s[head+1]]:
                res -= roman[s[head]]
            else:
                res += roman[s[head]]
            head += 1
        res += roman[s[head]]
        return res
