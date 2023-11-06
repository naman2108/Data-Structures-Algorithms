# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bt(self,root):
        if root is None:
            return (0,0)
        lft=self.bt(root.left)
        rgt=self.bt(root.right)
        op1=lft[0]
        op2=rgt[0]
        op3=lft[1]+rgt[1]
        ans=(max(op1,max(op2,op3)),max(lft[1],rgt[1])+1)
        return ans

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.bt(root)[0]
        