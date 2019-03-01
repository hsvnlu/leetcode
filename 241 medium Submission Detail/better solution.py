from collections import defaultdict

class Solution:
    _ops = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b
    }
    _cache = defaultdict(str)  # 全局初始化cache

    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        res = []
        if not input:
            return res
        if input in self._cache.keys():
            return self._cache[input]

        for i, ch in enumerate(input):
            if ch in self._ops.keys():
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                op = self._ops[ch]
                res += [op(l, r) for l, r in itertools.product(left, right)]
        if len(res) == 0:
            res.append(int(input))
        self._cache[input] = res
        return res
