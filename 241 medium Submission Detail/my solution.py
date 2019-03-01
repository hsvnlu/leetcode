'''
2019/3/1
hsvlu
runtime: 56ms 27.08%
memory: 13.2MB 6.00%
'''
class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            num = 0
            for ch in input:
                num = num * 10 + int(ch)
            return [num]
        
        output = []
        i = 0
        while i < len(input):
            if input[i].isdigit():
                i += 1
            else:   
                output1 = self.diffWaysToCompute(input[:i])
                output2 = self.diffWaysToCompute(input[i + 1:])
                for num1 in output1:
                    for num2 in output2:
                        output.append(self.Calculator(num1, num2, input[i]))
                i += 1
        return output
    
    def Calculator(self, num1, num2, opt):
        if opt == '+': return num1 + num2
        elif opt == '-': return num1 - num2
        else: return num1 * num2
