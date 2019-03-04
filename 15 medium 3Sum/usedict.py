'''
2019/3/4
runtime: 352ms 99.25%
memory: 17.4MB 10.47%
'''
class Solution:
    def threeSum(self, nums):
        pos, neg, cnt = [], [], {}
        for ele in nums:
            if ele in cnt:
                cnt[ele] += 1
            else:#在else中向pos，neg添加元素保证了没有重复
                cnt[ele] = 1
                if ele >= 0:
                    pos.append(ele)
                else:
                    neg.append(ele)
                    
        res = []
        if cnt.get(0,0) > 2:#dict.get(key[,default]),元素存在时，返回value，不存在时，返回default，default默认为None
            res.append([0,0,0])
            
        for p in pos:
            for n in neg:
                rest = - (p + n)
                if rest in cnt:
                    if rest > p or rest < n:#规定>,<保证了不会重复添加，如[-5,3,2]会出现两次
                        res.append([rest,n,p])
                    elif (rest == p or rest == n) and cnt[rest] > 1:#不会出现[0,0,0]，pos和neg只有一方含有0
                        res.append([rest,n,p])
        return res