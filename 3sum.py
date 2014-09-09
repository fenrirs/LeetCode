#https://oj.leetcode.com/problems/3sum/

'''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num)<3:
            return []
        res = []
        dict = {}
        for i in range(len(num)):
            if dict.get(num[i]):
                dict[num[i]] += 1
            else:
                dict[num[i]] = 1
        num = list(set(num))
        num.sort()
        x = 0
        while x<len(num) and num[x]<=0:
            y = x if dict[num[x]]>1 else (x+1)
            while y<len(num):
                if dict.get(-(num[x]+num[y])):
                    if num[y]<-(num[x]+num[y]):
                        res.append([num[x],num[y],-(num[x]+num[y])])
                    elif num[y]==-(num[x]+num[y]): 
                        if (num[y]==0 and dict[0]>2) or (num[y]!=0 and dict[num[y]]>1):
                            res.append([num[x],num[y],-(num[x]+num[y])])
                    else:
                        y = len(num)
                y += 1
            x += 1
        return res
