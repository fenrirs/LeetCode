#https://oj.leetcode.com/problems/palindrome-number/

'''Determine whether an integer is a palindrome. Do this without extra space.'''

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        digits = 1
        while x/digits>=10:
            digits *=10
        while digits>0 and x%10==x/digits:
            x = (x%digits)/10
            digits /= 100
        if x>0:
            return False
        return True
