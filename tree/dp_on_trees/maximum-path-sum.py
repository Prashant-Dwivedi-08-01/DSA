# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        res = [-float('inf')]
        self.solve(root, res)
        return res[0]
    def solve(self, root, res):
        if not root:
            return 0
        
        l = self.solve(root.left, res)
        r = self.solve(root.right, res)
        
        temp = max((max(l,r)+root.val), root.val)
        
        # agar present khud ans ka part banega toh ans kya aayega. Here ans is l+r+root.val 
        # but we select the maximum of temp ans ans, i.e. agar dono side se ans lene ke bajay
        # ek hi side se better ans aa raha hai( including node in both the cases)
        ans = max(temp, l+r+root.val) 
        
        res[0] = max(res[0], ans)
        
        return temp
