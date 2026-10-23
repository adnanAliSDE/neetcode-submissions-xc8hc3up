# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def helper(root):
            if root is None:
                return 0
            dl = helper(root.left)
            dr = helper(root.right)
            self.diameter = max(self.diameter, dl + dr)

            depth = max(dl, dr) + 1
            return depth
        helper(root)
        return self.diameter
