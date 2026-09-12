# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Index Map
        io_map = {}
        for idx, val in enumerate(inorder):
            io_map[val] = idx

        # Core logic
        def helper(po_range: tuple, io_range: tuple):
            po_start, po_end = po_range
            io_start, io_end = io_range
            if io_end == io_start:
                return

            root = TreeNode(preorder[po_start])
            root_idx = io_map[root.val]
            # inorder.pop(root_idx)

            left_io = (io_start, root_idx)
            left_po = (po_start + 1, po_start + 1 + left_io[1] - left_io[0])

            right_io = (root_idx+1, io_end )
            right_po = (po_start + 1 + left_io[1] - left_io[0], po_end + 1)

            root.left = helper(left_po, left_io)
            root.right = helper(right_po, right_io)
            return root
        n=len(preorder)

        return helper((0,n),(0,n))