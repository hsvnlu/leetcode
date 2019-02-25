"""
2019/2/25
hsvnlu
runtime: 88ms 45.43%
memory: 23.7MB 10.88%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        revrs = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, revrs = revrs, slow.next, slow
        if fast:
            slow = slow.next
        while slow and revrs:
            if slow.val != revrs.val: return False
            slow, revrs = slow.next, revrs.next
        return True
