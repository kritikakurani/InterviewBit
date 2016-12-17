# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def balanced(self, root):
        if root == None:
            return (True, 0)
        h1 = self.balanced(root.left)
        h2 = self.balanced(root.right)
        if h1[0] and h2[0] and abs(h1[1] - h2[1]) <= 1:
            return (True, 1 + max(h1[1], h2[1]))
        else:
            return (False, 1 + max(h1[1], h2[1]))

    def isBalanced(self, A):
        res = self.balanced(A)
        return res[0]