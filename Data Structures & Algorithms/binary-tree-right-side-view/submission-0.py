# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        levels = [] if root is None else [root.val]
        while True:
            level = deque([])
            while q:
                v = q.popleft()

                if v and v.left:
                    level.append(v.left)

                if v and v.right:
                    level.append(v.right)
            if level:
                levels.append(level[-1].val)
                q=level
            else:
                break
        return levels
