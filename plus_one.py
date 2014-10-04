#https://oj.leetcode.com/problems/plus-one/

'''Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        plus = 0
        temp = len(digits)-1
        while temp>=0:
            num = int(digits[temp])
            plus = (num+1)/10
            digits[temp] = (num+1)%10
            if plus:
                temp -= 1
            else:
                break
        if temp<0:
            return [1]+digits
        return digits
        
