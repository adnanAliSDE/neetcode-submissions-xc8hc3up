# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame=True
        if p is not None and q is None:
            isSame=False
        elif q is not None and p is None:
            isSame=False

        elif p is not None and q is not None:
            isSame = p.val==q.val
            isSame = isSame and self.isSameTree(p.left,q.left)
            isSame = isSame and  self.isSameTree(p.right,q.right)

        return isSame
