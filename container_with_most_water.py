#https://oj.leetcode.com/problems/container-with-most-water/

'''Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.'''

class Solution:
    # @return an integer
    def maxArea(self, height):
        a = [(x,i) for i,x in enumerate(height)]
        a.sort(reverse=True)
        n = len(height)
        minh = a[0][1]
        maxh = a[0][1]
        res = 0
        for i in range(n):
            dist = a[i][1]-minh if 2*a[i][1]>minh+maxh else maxh-a[i][1]
            res = max(res, a[i][0]*dist)
            minh = min(minh, a[i][1])
            maxh = max(maxh, a[i][1])
        return res
    
    # Another solution with O(n)    
    def maxArea1(self, height):
        l = 0
        r = len(height)-1
        res = 0
        while l<r:
            res = max(res,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return res
