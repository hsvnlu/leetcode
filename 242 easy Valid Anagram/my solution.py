'''
2019/3/1
hsvnlu
runtime: 60ms 64.53%
memory: 13.4MB 13.15%
'''
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sta = {}
        for ch in s:
            sta[ch] = sta.setdefault(ch, 0) + 1
        for ch in t:
            try:
                sta[ch] -= 1
            except:
                return False
        for i in sta.values():
            if i != 0: return False
        return True
