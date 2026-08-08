# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0

        def dfs(root):
            nonlocal maxHeight

            if not root:
                return 0
            
            left,right = dfs(root.left), dfs(root.right)

            maxHeight = max(maxHeight, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return maxHeight