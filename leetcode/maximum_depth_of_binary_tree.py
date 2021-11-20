from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # int (root)
        self.left = left    # TreeNode (child)
        self.right = right  # TreeNode (child)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)): # same level
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return depth
