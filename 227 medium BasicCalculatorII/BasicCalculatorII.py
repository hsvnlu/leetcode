"""
2017/2/17
hsvnlu
time: 144ms 74.56%
space: 7.1MB 100%
"""
class Solution:
    def calcu_two_num(self, a, b, opt):
        if opt == '+': return a + b
        elif opt == '-': return a - b
        elif opt == '/': return a // b
        else: return a * b
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += 'u'
        opt_rank = {'+': 0, '-': 0, '*': 1, '/': 1}
        opt_stack = []
        num_stack = []
        numend = True
        for char in s:
            if char.isdigit():
                if numend: num_stack.append(int(char))
                else: num_stack[-1]  = num_stack[-1] * 10 + int(char)
                numend = False
            elif char != ' ':
                numend = True
                opt_stack.append(char)
                if len(opt_stack) > 2:
                    if opt_rank[opt_stack[-2]] > opt_rank[opt_stack[-3]]:
                        num_stack[-2:] = (self.calcu_two_num(num_stack[-2], num_stack[-1], opt_stack[-2]),)
                        del opt_stack[-2]
                    else:
                        num_stack[-3:-1] = (self.calcu_two_num(num_stack[-3], num_stack[-2], opt_stack[-3]),)
                        del opt_stack[-3]
            else:
                numend = True
        if len(num_stack) == 1: return num_stack[0]
        else: return self.calcu_two_num(num_stack[-2], num_stack[-1], opt_stack[-2])
