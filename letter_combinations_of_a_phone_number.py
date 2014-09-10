#https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

'''Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''




class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letterMap = {
            '1':'','2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '
        }
        if digits==None:
            return ['']
        res = ['']
        for digit in digits:
            res = [s+letter for s in res for letter in letterMap[digit]]
        return res
