"""
2019/2/18
hsvnlu
time: 40ms 100%
space: 6.4MB 76.19%
"""
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        start = end = nums[0]
        nums.append(nums[-1] + 2)
        summary = []
        for num in nums:
            if num - end <= 1:
                end = num
            else:
                if start == end:
                    summary.append(str(start))
                else:
                    summary.append(str(start) + "->" + str(end))
                start = end = num
        return summary
