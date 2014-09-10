#https://oj.leetcode.com/problems/4sum/

'''Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4:
            return []
        num.sort()
        dict = {}
        lenn = len(num)
        for i in range(0,lenn-1):
            for j in range(i+1,lenn):
                if num[i]+num[j] not in dict:
                    dict[num[i]+num[j]] = set()
                dict[num[i]+num[j]].add((num[i],num[j]))
        
        res = set()
        for x in dict.keys():
            if 2*x>target:
                continue
            y = target-x
            if y in dict:
                for i in dict[x]:
                    for j in dict[y]:
                        #if i==j and not((i[0]!=i[1] and num.count(i[0])>1 and num.count(i[1])>1) or (i[0]==i[1] and num.count(i[0])>3)):
                            #continue
                        temp = list(i+j)
                        temp.sort()
                        flag = True
                        for k in range(4):
                            if temp.count(temp[k])>num.count(temp[k]):
                                flag = False
                        if flag:
                            res.add(tuple(temp))
        return map(list,res)
        
if __name__=='__main__':
	s = Solution()
	print s.fourSum([-3,-1,0,2,4,5], 0)
	print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)
