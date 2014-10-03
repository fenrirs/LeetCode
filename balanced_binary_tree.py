#https://oj.leetcode.com/problems/balanced-binary-tree/

'''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.'''

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def checkBalance(self,root):
        if not root:
            return True,0
        flag1,h1 = self.checkBalance(root.left)
        flag2,h2 = self.checkBalance(root.right)
        if not flag1 or not flag2 or abs(h1-h2)>1:
            return False,-2
        return True,max(h1,h2)+1
        
    def isBalanced(self, root):
        flag,depth = self.checkBalance(root)
        return flag
