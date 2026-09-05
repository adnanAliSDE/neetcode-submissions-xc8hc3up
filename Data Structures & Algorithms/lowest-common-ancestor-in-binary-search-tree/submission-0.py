# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        self.lca = None

        def helper(node):
            if self.lca:
                return
   
            if node is not None:
                helper(node.left)
                helper(node.right)
                if self.isPresent(node, p) and self.isPresent(node, q):
                    if self.lca is None:
                        self.lca = node

        helper(root)
        return self.lca

    def isPresent(self, root, child):
        if not child:
            return True
        if not root:
            return False

        return (
            root.val == child.val
            or self.isPresent(root.left, child)
            or self.isPresent(root.right, child)
        )
