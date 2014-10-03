#https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/

'''Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def traverse(self,root,depth):
        if not root.left and not root.right:
            self.res += int(''.join(self.str[:depth]))
        for nextNode in (root.left,root.right):
            if nextNode!=None:
                if depth>=len(self.str):
                    self.str.append(str(nextNode.val))
                else:
                    self.str[depth] = str(nextNode.val)
                self.traverse(nextNode,depth+1)
        
    def sumNumbers(self, root):
    	if not root:
    		return 0
        self.res = 0
        self.str = [str(root.val)]
        self.traverse(root,1)
        return self.res
