"""
2019/2/25
hsvnlu
runtime:84ms 80.91%
memory: 17.4MB 5.18%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val: p, q = q, p
        anc = root
        while True:
            if q.val < anc.val: anc = anc.left
            elif p.val > anc.val: anc = anc.right
            else: return anc
