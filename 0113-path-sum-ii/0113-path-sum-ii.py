
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]

        def dfs(node,path,target):
            
            if not node:
                return

            path.append(node.val)
            target+=node.val
            
            if not node.left and not node.right:
                if targetSum==target:
                    ans.append(path[:])
                
            dfs(node.left,path  , target)
            dfs(node.right,path  , target)

            path.pop()
        dfs(root,[],0)
     
        return ans
        