'''
2019/2/25
hsvnlu
runtime: 84ms 83.16%
memory: 17.4MB 79.72%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parents = {root:None}
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
        ancestor = []
        while p in parents:
            ancestor.append(p)
            p = parents[p]
        while q not in ancestor:
            q = parents[q]
        return q
