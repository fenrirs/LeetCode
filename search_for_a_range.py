#https://oj.leetcode.com/problems/search-for-a-range/

'''Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1,-1]
        left,right = 0,len(A)-1
        while left<right:
            mid = (left+right+1)/2
            if A[mid]<target:
                left = mid
            else:
                right = mid-1
        if left==0 and A[left]==target:
            p1 = left
        elif left==len(A)-1 or A[left+1]!=target:
            return [-1,-1]
        else:
            p1 = left+1
        
        left,right = 0,len(A)-1
        while left<right:
            mid = (left+right)/2
            if A[mid]>target:
                right = mid
            else:
                left = mid+1
        if right==len(A)-1 and A[right]==target:
        	p2 = right
        elif right==0 or A[right-1]!=target:
            return [-1,-1]
        else:
            p2 = right-1
        return [p1,p2]
