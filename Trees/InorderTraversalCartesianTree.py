# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if A:
            idx = A.index(max(A))
            root = TreeNode(A[idx])
            root.left = self.buildTree(A[:idx])
            root.right = self.buildTree(A[idx+1:])
            return root
