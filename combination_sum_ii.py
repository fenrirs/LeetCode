#https://oj.leetcode.com/problems/combination-sum-ii/

'''Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] '''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        def calc(tail,n,sum):
            if not sum:
                res.add(tuple(a[:n]))
            for i in range(tail+1,lenC):
                if candidates[i]<=sum:
                    if n>=len(a):
                        a.append(candidates[i])
                    else:
                        a[n] = candidates[i]
                    #print a[:n+1]
                    calc(i,n+1,sum-candidates[i])
            
        candidates.sort()
        #print candidates
        lenC = len(candidates)
        #print lenC
        res = set()
        a = []
        calc(-1,0,target)
        return [list(a) for a in res]
