# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        else:
            matches=[]
            def inOrder(node):
                if node is not None:
                    yield from inOrder(node.left)
                    yield node
                    yield from inOrder(node.right)

            for node in inOrder(root):
                if node.val==subRoot.val:
                    matches.append(node)
        
            subTree=[]
            for node in inOrder(subRoot):
                subTree.append(node.val)

    
            sentinel=object()
            while matches:
                gen=inOrder(matches.pop())
                did_break=False
                node = next(gen,sentinel)
                for i in range(len(subTree)):
                    if node is sentinel:
                        did_break=True
                        break
                    if subTree[i]!=node.val:
                        did_break=True
                        break
                    node=next(gen,sentinel)
                
                if (not did_break) and (node is sentinel):
                    return True

            return False