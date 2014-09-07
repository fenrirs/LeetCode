#https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

'''Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        lastAppears = {}
        head = -1
        maxLen = 0
        for i in range(len(s)):
            lastAppear = lastAppears.get(s[i])
            if (lastAppear!=None)and(head<lastAppear) :
                head = lastAppear
            maxLen = max(maxLen, i-head)
            lastAppears[s[i]]=i
        return maxLen;
