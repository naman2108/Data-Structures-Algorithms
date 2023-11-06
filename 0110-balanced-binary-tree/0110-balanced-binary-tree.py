# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        lft=self.height(root.left)
        rgt=self.height(root.right)
        return max(lft,rgt)+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lft=self.isBalanced(root.left)
        rgt=self.isBalanced(root.right)
        third=abs(self.height(root.left)-self.height(root.right))
        return True if lft and rgt and third<=1 else False