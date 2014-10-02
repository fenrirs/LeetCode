#https://oj.leetcode.com/problems/jump-game-ii/

'''Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A:
            return 0
        MAXINT =  2147483647
        lenA = len(A)
        steps = [MAXINT for i in range(lenA)]
        steps[0] = 0
        maxStep = 0
        for i in range(lenA-1):
            t = min(i+A[i]+1,lenA)
            for tempStep in range(maxStep+1,t):
                steps[tempStep] = min(steps[tempStep],steps[i]+1)
            maxStep = max(maxStep,i+A[i])
        return steps[lenA-1]

