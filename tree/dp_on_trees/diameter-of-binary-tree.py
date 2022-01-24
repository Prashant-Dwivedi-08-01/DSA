# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = [-float('inf')] #! this is brilliant work around for passing things by refrence in python
        self.solve(root, res)
        return res[0]-1
    def solve(self, root, res):
        #base condition
        if root is None:
            return 0

        #hypothesis
        l = self.solve(root.left, res) # ans from left subtree
        r = self.solve(root.right, res) # ans from right subtree
        
        #induction

        # When we are saying the ans is above the root. So we take max of both sides and then add 1 for present
        # node ans then we pass this for future calculations
        temp = 1 + max(l, r) 
        
        # This is the ans at present node. We are not passing above but considering that rightSubtree-presentRoot-leftSubtree 
        # is the only answer
        ans = max(temp, 1+l+r) 
        
        # here we select the best answer, i.e. we update our original answer if the new ans obtained is better
        res[0] = max(res[0], ans) 
        
        return temp