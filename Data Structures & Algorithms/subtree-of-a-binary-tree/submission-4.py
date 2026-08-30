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
            def inOrder(node):
                if node is not None:
                    yield from inOrder(node.left)
                    yield node
                    yield from inOrder(node.right)

            subTree = []
            def compareHelper(matchNode)->bool:
                sentinel = object()

                gen = inOrder(matchNode)
                did_break = False
                node = next(gen, sentinel)
                for i in range(len(subTree)):
                    if node is sentinel:
                        did_break = True
                        break
                    if subTree[i] != node.val:
                        did_break = True
                        break
                    node = next(gen, sentinel)

                if (not did_break) and (node is sentinel):
                    return True
                else:
                    return False

            for node in inOrder(subRoot):
                subTree.append(node.val)

            for node in inOrder(root):
                if node.val == subRoot.val:
                    isSubTree= compareHelper(node)
                    if isSubTree:
                        return True

            return False
