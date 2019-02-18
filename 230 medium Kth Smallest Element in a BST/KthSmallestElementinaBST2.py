"""
2019/2/18
hsvnlu
time: 72ms 93.18%
space: 11MB 93.85%
"""

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
        def _inorderTraversal(root, nodes):
            if root:
                _inorderTraversal(root.left, nodes)
                nodes.append(root.val)
                if len(nodes) >= k: return
                _inorderTraversal(root.right, nodes)
            return
        _inorderTraversal(root, nodes)
        return nodes[k - 1]
