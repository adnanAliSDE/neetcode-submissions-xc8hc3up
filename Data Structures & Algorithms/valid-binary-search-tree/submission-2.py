# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.min_val = -float("inf")
        self.isValid = True

        def helper(node):
            if node and self.isValid:
                helper(node.left)
                if node.val <= self.min_val:
                    self.isValid = False
                    return 
                self.min_val=node.val
                helper(node.right)

        helper(root)
        return self.isValid
