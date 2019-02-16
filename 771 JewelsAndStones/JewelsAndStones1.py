"""
2017/2/16
hsvnlu
time: 48ms 97.32%
spaces: 6.5MB 74.82%
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for i in range(len(J)):
            n += S.count(J[i])
        return n
