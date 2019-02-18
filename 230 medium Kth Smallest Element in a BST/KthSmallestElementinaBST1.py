"""
2019/2/18
hsvnlu
time: 76ms 86.35%
space: 11.1MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes = []
        self.inorderTraversal(root, nodes)
        return nodes[k - 1]
        
    def inorderTraversal(self,root, nodes):
        if root:
            self.inorderTraversal(root.left, nodes)
            nodes.append(root.val)
            self.inorderTraversal(root.right, nodes)
        return nodes
