from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root: TreeNode):
            if not root: # check leaf
                return -1

            left = dfs(root.left)   # to the left leaf node
            right = dfs(root.right) # to the right leaf node
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return self.longest
