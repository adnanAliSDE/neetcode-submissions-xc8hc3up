
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        if root is not None:
            arr.extend(self.postorderTraversal(root.left))
            arr.extend(self.postorderTraversal(root.right))
            arr.append(root.val)
        return arr