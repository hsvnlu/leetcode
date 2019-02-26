'''
2019/2/26
hsvnlu
runtime: 104ms 97.58%
memory: 19.9MB 5.85%
'''
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k <= 1: return nums
        n = len(nums)
        maxid = -1
        output = [0] * (n - k + 1)
        for i in range(n - k + 1):
            if maxid < i:
                maxid = i
                for j in range(i, i + k):
                    if nums[j] >= nums[maxid]: maxid = j
            else:
                if nums[maxid] < nums[i + k - 1]:
                    maxid = i + k - 1
            output[i] = nums[maxid]
        return output
