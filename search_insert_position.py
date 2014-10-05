#https://oj.leetcode.com/problems/search-insert-position/

'''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        def binarySearch(h,t,val):
            if h==t:
                if A[h]==val:
                    self.res = h
                    return 
                else:
                    self.res = h+1 if A[h]<val else h
                    return 
            mid = (h+t)/2
            if A[mid]>val:
                binarySearch(h,mid,val)
            elif A[mid]==val:
                self.res = mid
                return 
            else:
                binarySearch(mid+1,t,val)
        
        binarySearch(0,len(A)-1,target)
        return self.res
