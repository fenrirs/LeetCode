#https://oj.leetcode.com/problems/implement-strstr/

'''Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        lenH = len(haystack)
        lenN = len(needle)
        for i in range(lenH-lenN+1):
            if haystack[i:i+lenN]==needle:
                return haystack[i:]
        return None
