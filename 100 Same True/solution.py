"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # ---------------- Solution 0 -----------
        if p == None: 
            if q == None:
                return True
            else:
                return False
        if q == None:
            return False 
        
        if p.val != q.val:
            return False
        
        b1 = False
        b2 = False
        if p.left and q.left:
            b1 = self.isSameTree(p.left, q.left)
        if p.left == None and q.left == None:
            b1 = True
            
        if p.right and q.right:
            b2 = self.isSameTree(p.right, q.right)
        if p.right == None and q.right == None:
            b2 = True
            

        return b1 and b2