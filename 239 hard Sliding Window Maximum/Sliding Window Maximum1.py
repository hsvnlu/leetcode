'''
2019/2/26
hsvnlu
runtime: 124ms 62.95%
memory: 19.7MB 5.85%
'''
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k <= 1: return nums
        deque = [0]
        output = []
                
        for i in range(1, len(nums)):
            if i >= k and deque[0] <= i - k:
                del deque[0]
            if nums[i] > nums[deque[0]]: deque[:] = [i]
            else:
                while nums[i] > nums[deque[-1]]:
                    deque.pop()
                deque.append(i)
            if i >= k - 1:
                output.append(nums[deque[0]])
        return output           
