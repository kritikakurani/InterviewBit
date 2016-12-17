# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx],postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:],postorder[idx:-1])
        return root
