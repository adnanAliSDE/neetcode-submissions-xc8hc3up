# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        curr_level = 0

        def helper(node, parent=None, left=True,parent_level=0):
            if not parent:
                res.append([node.val])
            else:
                level_elems=[]
                if left: 
                    level_elems = [node.val]
                    if parent.right:
                        level_elems.append(parent.right.val)
                else:
                    if not parent.left:
                        level_elems=[node.val]


                if len(res)>parent_level:
                    res[parent_level].extend(level_elems)
                else:
                    res.append(level_elems)

            parent_level=parent_level+1
            if node.left:
                helper(node.left,node,parent_level=parent_level)
            if node.right:
                helper(node.right,node,left=False,parent_level=parent_level)

        if root is None:
            return []
        helper(root)
        return res
