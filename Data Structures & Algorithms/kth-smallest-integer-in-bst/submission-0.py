# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.idx = 1
        self.res = None

        def helper(node):
            if node is not None and self.idx <= k:
                helper(node.left)
                if self.idx == k:
                    self.res = node.val
                    self.idx += 1
                    return node.val
                self.idx += 1
                helper(node.right)

        helper(root)
        return self.res