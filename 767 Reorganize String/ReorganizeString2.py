class Solution:
    def reorganizeString(self, S):
        """
        2019/2/16
        hsvnlu
        time: 48ms
        space: 6.5MB
        :type S: str
        :rtype: str
        """
        a = sorted(sorted(S), key = S.count)
        half = len(S) // 2
        a[::2], a[1::2] = a[half:], a[:half]
        if a[-1] == a[-2]: return ""
        else: return "".join(a)  
