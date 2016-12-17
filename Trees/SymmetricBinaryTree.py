# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def symmetric(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)

    def isSymmetric(self, A):
        return self.symmetric(A.left, A.right)
