# leetcode

注：每个二级标题连接到leetcode网站上对应的问题
## [1 Two Sum](https://leetcode.com/problems/two-sum/)
[mysolution.py](https://github.com/hsvnlu/leetcode/blob/master/1%20easy%20TwoSum/mysolution.py)

时间复杂度$O(n^{2})$

*two pointer*的思想，一种高效的遍历
```python
s = nums[low] + nums[high]
if s < target:
    low += 1
elif s > target:
    high -= 1
```
[usedict.py](https://github.com/hsvnlu/leetcode/blob/master/1%20easy%20TwoSum/usedict.py)

在python中，dict是用散列的方式存储的，按key查找速度非常快。

## [15 3Sum](https://leetcode.com/problems/3sum/)
[translateto2sum](https://github.com/hsvnlu/leetcode/blob/master/1%20medium%203Sum/translatetosum.py)

三个指针固定一个（这里是第一个），之后仍旧是*two pointer*思想，转化为2sum问题

[usedict](https://github.com/hsvnlu/leetcode/blob/master/1%20medium%203Sum/usedict.py)

还是利用了字典查找速度快的特性

要避免输出结果重复，可以为其添加“序”来避免
```python
for p in pos:
    for n in neg:
        rest = - (p + n)
        if rest in cnt:
            if rest > p or rest < n:#规定>,<保证了不会重复添加，如[-5,3,2]会出现两次
                res.append([rest,n,p])
            elif (rest == p or rest == n) and cnt[rest] > 1:#不会出现[0,0,0]，pos和neg只有一方含有0
                res.append([rest,n,p])
```
为使代码易读，变量可以在使用之前再声明

## [227 Basic CalculatorII](https://leetcode.com/problems/basic-calculator-ii/)

229 230 231 234 236 238
