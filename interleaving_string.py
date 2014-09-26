#https://oj.leetcode.com/problems/interleaving-string/

'''Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = [[False for col in range(len(s2)+1)] for row in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i>0:
                    dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) 
                if j>0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len(s1)][len(s2)]
                
