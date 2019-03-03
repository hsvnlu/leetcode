'''
2019/3/2
runtime: 44ms 64.89%
memory: 14.9MB 5.08%
'''
from operator import itemgetter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key = itemgetter(1))
        low = 0
        high = len(nums) - 1
        while low < high:
            s = nums[low][1] + nums[high][1]
            if s < target:
                low += 1
            elif s > target:
                high -= 1
            else:
                return [nums[low][0], nums[high][0]]
            while low < high - 1 and nums[low][0] == nums[low + 1][0]:
                low += 1
            while high > low + 1 and nums[high][0] == nums[high - 1][0]:
                high -= 1
        return []
