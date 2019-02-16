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
