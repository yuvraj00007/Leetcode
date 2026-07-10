
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k-1]
