#https://oj.leetcode.com/problems/3sum-closest/

'''Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''
    
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num)==0:
            return 0
        if len(num)<4:
            return sum(num)
        num.sort()
        lenn = len(num)
        res = num[0]+num[1]+num[2]-target
        for i in range(0,lenn-2):
            j = i+1
            k = lenn-1
            while j<k:
                s = num[i]+num[j]+num[k]-target
                if abs(s)<abs(res):
                    res = s
                if s<0:
                    j += 1
                elif s>0:
                    k -= 1
                else:
                    return target
        return res+target
