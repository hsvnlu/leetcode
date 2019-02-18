"""
2019/2/18
hsvnlu
time: 68ms 43.64%
space: 7.5MB 94.23%
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = [0, 0]
        vote = [0, 0]
        res = []
        for item in nums:
            if item in num:
                vote[num.index(item)] += 1
            elif 0 in vote:
                pos = vote.index(0)
                num[pos] = item
                vote[pos] += 1
            else:
                vote[0] -= 1
                vote[1] -= 1
        appear = len(nums) // 3
        if nums.count(num[0]) > appear: res.append(num[0])
        if nums.count(num[1]) > appear and num[0] != num[1]: res.append(num[1])
        return res
