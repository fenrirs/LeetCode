#https://oj.leetcode.com/problems/trapping-rain-water/

'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        left,right = 0,len(A)-1
        lmax,rmax = A[left],A[right]
        res = 0
        while left<right:
            if A[left]<=A[right]:
                res += max(0,min(lmax,rmax)-A[left])
                left += 1
                lmax = max(lmax,A[left])
            else:
                res += max(0,min(lmax,rmax)-A[right])
                right -= 1
                rmax = max(rmax,A[right])
        return res
