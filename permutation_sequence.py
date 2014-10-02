#https://oj.leetcode.com/problems/permutation-sequence/

'''The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        waitList = [i+1 for i in range(n)]
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        if k>fac[n]:
            return ''
        k -= 1
        res = ''
        for i in range(n):
            d,m = divmod(k,fac[n-1-i])
            res += str(waitList[d])
            waitList.remove(waitList[d])
            k = m
        return res
