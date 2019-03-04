'''
2019/3/3
hsvnlu
runtime: 932ms 69.43%
memory: 16.8MB 22.9%
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s < 0:
                    low += 1
                elif s > 0:
                    high -= 1
                else:
                    output.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while high > low and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1; high -= 1
        return output