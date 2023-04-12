from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            left_child = self.isSameTree(p.left, q.left)
            right_child = self.isSameTree(p.right, q.right)
            return p.val == q.val and left_child and right_child
        return False
