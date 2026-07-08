# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(p):
            if p==None:
                return 0
            ld=helper(p.left)
            rd=helper(p.right)
            if ld==0 or rd==0:
                return ld+rd+1
            else:
                return min(ld,rd)+1
        return helper(root)