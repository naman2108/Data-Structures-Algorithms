from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lot(self, root):
        if root:
            ans = []
            q = deque([root])
            while q:
                node = q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return ans

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root  # Return the current node, not the result of lot(val)

        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Example usage:
# Assuming you have a tree defined, e.g., root = TreeNode(5, left=TreeNode(3), right=TreeNode(7))
# solution = Solution()
# result = solution.searchBST(root, 3)
# print(result.val)  # Output should be 3
