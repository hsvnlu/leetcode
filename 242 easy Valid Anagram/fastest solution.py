class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
    
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True
