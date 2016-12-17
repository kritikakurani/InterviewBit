# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer

    def kthsmallest(self, root, k):
        res,stack = [],[]
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            while curr == None and stack:
                curr = stack.pop(-1)
                res.append(curr.val)
                curr = curr.right
            if curr == None and not stack:
                break
        return res[k-1]