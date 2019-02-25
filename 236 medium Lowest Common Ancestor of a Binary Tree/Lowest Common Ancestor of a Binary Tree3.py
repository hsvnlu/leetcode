# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """  
    #     if not root or root is p or root is q: 
    #         return root
    #     left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
    #     if left and right: 
    #         return root
    #     return left or right


    def __init__(self):
        self.memo = {}
    def isChild(self, root, node):
        if (root, node) in self.memo:
            return self.memo[(root, node)]
        if root is None:
            return False
        if root == node:
            return True
        ret = self.isChild(root.left, node) or self.isChild(root.right, node)
        self.memo[(root, node)] = ret
        return ret
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if (root == p or root == q):
            return root
        
        if self.isChild(p, q):
            return p
        if self.isChild(q, p):
            return q
        
        def helper(root, p, q):
            pIsLeft = self.isChild(root.left, p)
            qIsRight = self.isChild(root.right, q)

            if (pIsLeft and qIsRight) or (not pIsLeft and not qIsRight):
                return root

            if (pIsLeft):
                return self.lowestCommonAncestor(root.left, p, q)
            return self.lowestCommonAncestor(root.right, p, q)
        
        return helper(root, p, q)
