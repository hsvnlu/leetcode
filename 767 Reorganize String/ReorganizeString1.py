class Solution:
    def reorganizeString(self, S):
        """
        16.02.2019
        hsvnlu
        time: 52ms
        space: 6.4MB
        :type S: str
        :rtype: str
        Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
		If possible, output any possible result.  If not possible, return the empty string.
        """
        a = {i: S.count(i) for i in S}
        a = sorted(a.items(), key = lambda item:item[1], reverse = True)
        if a[0][1] > int((len(S) + 1)/2): return ""
        
        b = []
        for i in range(len(a)):
            for j in range(a[i][1]):
                b.append(a[i][0])
        x = b[:int((len(b) + 1) / 2)]
        y = b[int((len(b) + 1) / 2):]
        for i in range(len(y)):
            x.insert(i * 2 + 1, y[i])                                               
        return ''.join(x)
