'''
2019/2/26
hsvnlu
runtime: 108ms 47.90%
memory: 20.9MB 5.12%
'''
class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        p = 1
        output = []
        for i in range(l):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(l - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output
