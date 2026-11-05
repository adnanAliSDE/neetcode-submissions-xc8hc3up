# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def helper(root, max_val=-float("inf")):
            if root is not None:
                max_val = max(root.val, max_val)
                if root.val == max_val:
                    self.res += 1
                helper(root.left, max_val)
                helper(root.right, max_val)

        helper(root)
        return self.res
