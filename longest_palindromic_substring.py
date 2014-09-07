#https://oj.leetcode.com/problems/longest-palindromic-substring/

'''Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        s1 = '#'+'#'.join(s)+'#'
        len1 = len(s1)
        p={}
        id = 0
        mx = 0
        for i,x in enumerate(s1):
            p[i] = min(p[2*id-i],mx-i) if mx>i else 1
            while i+p[i]<len1 and i-p[i]>-1 and s1[i+p[i]]==s1[i-p[i]]:
                p[i] = p[i]+1
            if i+p[i]>mx:
                mx = i+p[i]
                id = i
        id = 0
        mx = 0
        for i in range(len1):
            if p[i]>mx:
                id = i
                mx = p[i]
        return s[(id-mx+1)/2:(id+mx)/2]
