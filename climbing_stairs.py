#https://oj.leetcode.com/problems/climbing-stairs/

'''You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = [1,1]
        for i in range(2,n+1):
            f.append(f[-1]+f[-2])
        return f[-1]
