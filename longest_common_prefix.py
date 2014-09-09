#https://oj.leetcode.com/problems/longest-common-prefix/

'''Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n==0:
            return ''
        minlen = min(len(strs[i]) for i in range(n))
        if minlen==0:
            return ''
        for i in range(minlen):
            char = strs[0][i]
            for j in range(n):
                if strs[j][i]!=char:
                    return strs[0][:i] if i>0 else ''
        return strs[0][:minlen]
