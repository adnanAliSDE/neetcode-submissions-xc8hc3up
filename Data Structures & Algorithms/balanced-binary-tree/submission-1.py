# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return 0, True

            is_balanced = 1, True
            lh, is_left_balanced = helper(root.left)
            is_balanced = is_balanced and is_left_balanced
            if is_balanced:
                rh, is_right_balanced = helper(root.right)
                height = max(lh, rh) + 1
                is_balanced = is_left_balanced and is_right_balanced and abs(lh - rh) <= 1
            else:
                height = 1 + lh
            return height, is_balanced

        return helper(root)[-1]
