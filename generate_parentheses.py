#https://oj.leetcode.com/problems/generate-parentheses/

'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []
        
        def generate(length,balance,s):
            if length==2*n:
                if balance==0:
                    res.append(s)
                return
            if balance>0:
                generate(length+1,balance-1,s+')')
            if balance<n:
                generate(length+1,balance+1,s+'(')
        
        generate(0,0,'')
        return(res)
