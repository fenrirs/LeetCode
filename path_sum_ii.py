#https://oj.leetcode.com/problems/path-sum-ii/

'''Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    # Do not take valList into recursion, otherwise you would get a TLE
    def checkRoute(self,node,length,sum):
        if sum==node.val and (not node.left) and (not node.right):
            self.res.append(self.valList[:length])
            return
        for nextNode in (node.left,node.right):
            if nextNode!=None:
                if len(self.valList)<=length:
                    self.valList.append(nextNode.val)
                else:
                    self.valList[length] = nextNode.val
                self.checkRoute(nextNode,length+1,sum-node.val)

    def pathSum(self, root, sum):
        if not root:
            return []
        self.res = []
        self.valList = [root.val]
        self.checkRoute(root,1,sum)
        return self.res
