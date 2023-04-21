from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        def symmetric_helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and symmetric_helper(left.left, right.right) and symmetric_helper(left.right, right.left)

        if not root:
            return True

        return symmetric_helper(root.left, root.right)
