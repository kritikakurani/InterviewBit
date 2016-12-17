# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if A == ():
            return None
        n = len(A)
        idx = int(n/2)
        root = TreeNode(A[idx])
        root.left = self.sortedArrayToBST(A[:idx])
        root.right = self.sortedArrayToBST(A[idx+1:])
        return root