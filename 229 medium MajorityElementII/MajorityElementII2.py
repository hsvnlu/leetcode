"""
2019/2/18
hsvnlu
time: 52ms 100%
space: 7.5MB 86.54%
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return [x for x in set(nums) if nums.count(x)>int(n/3)]
