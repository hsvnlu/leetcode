"""
2019/2/19
hsvnlu
runtime: 48ms 100%
memory: 12.6MB 100%
"""
class Solution:
    def isPowerOfTwo(self, n: 'int') -> 'bool':
    return n > 0 and (n & n - 1 == 0)
