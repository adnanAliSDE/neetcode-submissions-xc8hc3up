"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr=[]
        if root is not None:
            for child in root.children:
                arr.extend(self.postorder(child))
            arr.append(root.val)
        return arr