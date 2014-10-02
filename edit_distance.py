#https://oj.leetcode.com/problems/edit-distance/

'''Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        len1,len2 = len(word1),len(word2)
        dist = [[0 for i in range(len2+1)] for j in range(len1+1)]
        for i in range(len1+1):
            dist[i][0] = i
        for j in range(len2+1):
            dist[0][j] = j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                f = 0 if word1[i-1]==word2[j-1] else 1
                dist[i][j] = min(dist[i-1][j]+1,dist[i][j-1]+1,dist[i-1][j-1]+f)
        return dist[len1][len2]
        
