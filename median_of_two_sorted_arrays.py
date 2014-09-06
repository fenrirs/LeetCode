#https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

'''There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).'''

#It's interesting that O(n+m) with cpp takes 228ms, while O(log(n+m)) with python takes 656ms

class Solution:
    # @return a float
    def getKth(self,A,B,k):
        m = len(A)
        n = len(B)
        if m>n:
            return self.getKth(B,A,k)
        if len(A)==0:
            return B[k-1]
        if k==1:
            return min(A[0],B[0])
        q1 = min(m,k/2)
        q2 = min(n,k/2)
        if A[q1-1]<B[q2-1]:
            return self.getKth(A[q1:],B,k-q1)
        else:
            return self.getKth(A,B[q2:],k-q2)
    
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        mid = (m+n)/2
        if (m+n)%2==1:
            return self.getKth(A,B,mid+1)
        else:
            return 0.5*(self.getKth(A,B,mid)+self.getKth(A,B,mid+1))
