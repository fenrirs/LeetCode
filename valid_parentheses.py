#https://oj.leetcode.com/problems/valid-parentheses/

'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        cp={')':'(', '}':'{', ']':'['}
        list = []
        for ch in s:
            if ch in ['(','{','[']:
                list.append(ch)
            else:
                if len(list)==0 or cp[ch]!=list[-1]:
                    return False
                list.pop()
        if len(list)!=0:
            return False
        return True
