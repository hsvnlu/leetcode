'''
2019/2/25
hsvnlu
runtime: 108ms 33.48%
memory: 28MB 12.58%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def PreTraversal(root, nlr):
            if root:
                nlr.append(root)
                PreTraversal(root.left, nlr)
                PreTraversal(root.right, nlr)
            return

        def InTraversal(root, lnr):
            if root:
                InTraversal(root.left, lnr)
                lnr.append(root)
                InTraversal(root.right, lnr)
            return
        nlr = []
        lnr = []
        PreTraversal(root, nlr)
        InTraversal(root, lnr)
        l1 = nlr.index(p)
        r1 = nlr.index(q)
        if l1 > r1: l1, r1 = r1, l1
        l2 = lnr.index(p)
        r2 = lnr.index(q)
        if l2 > r2: l2, r2 = r2, l2
            
        c = [x for x in nlr[:l1] if x in lnr[l2 + 1:r2]]
        if len(c) > 0: return c[0]
        else: return nlr[l1]
